from fastapi import FastAPI, Request
from prometheus_client import CollectorRegistry, Summary, push_to_gateway
from starlette.responses import RedirectResponse

from . import v1

app = FastAPI(
    title="Algorithms API",
    description="Calculate results for some algorithms.",
    version="0.0.1",
    docs_url="/",
)
registry = CollectorRegistry()
request_time = Summary(
    "request_processing_seconds", "Time spent processing request", registry=registry
)


@app.middleware("http")
async def add_summary_to_prometheus(request: Request, call_next):
    with request_time.time():
        response = await call_next(request)
        try:
            push_to_gateway("pushgateway:9091", job="algo-api", registry=registry)
        except:
            # We don't want to break API if monitoring is broken
            pass
        return response


@app.get("/docs", name="Openapi UI", tags=["utils"])
async def docs_url():
    return RedirectResponse("/")


@app.get(
    "/healthcheck",
    name="Health check",
    description="Check health of the service.",
    tags=["utils"],
)
async def healthcheck() -> dict:
    return {"msg": "OK"}


app.include_router(v1.router, prefix="/v1")
