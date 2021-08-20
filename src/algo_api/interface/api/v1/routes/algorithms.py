from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from algo_api.algorithms.fibonacci import fib_iter

router = APIRouter()


@router.get(
    "/algorithms/fibonacci",
    name="Calculate Fibonacci number",
    description="Calculate Fibonacci number for the given input using iterative approache",
    tags=["algorithms"],
    operation_id="calculateFibonacci",
    response_model=int,
    status_code=200,
)
def fibonacci(n: int) -> int:
    if n < 0:
        raise HTTPException(
            status_code=422, detail=f"Can't calculate Fibonacci number for negative integers."
        )

    try:
        return fib_iter(n)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Something went wrong while calculateing fibonacci of {n}"
        ) from e
