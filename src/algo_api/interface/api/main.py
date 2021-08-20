from fastapi import FastAPI
from starlette.responses import RedirectResponse

from . import v1

app = FastAPI(
    title="Algorithms API",
    description="Calculate results for some algorithms.",
    version="0.0.1",
    docs_url="/",
)


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
