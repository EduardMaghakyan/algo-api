from typing import Optional
from typing import Optional

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from algo_api.algorithms import ackermann, factorial, fib_iter

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
def handle_fibonacci(n: int) -> Optional[int]:
    if n < 0:
        raise HTTPException(
            status_code=422, detail=f"Can't calculate Fibonacci number for negative integers."
        )

    try:
        return fib_iter(int(n))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Something went wrong while calculateing fibonacci of {n}"
        ) from e


@router.get(
    "/algorithms/ackermann",
    name="Calculate Ackermann number",
    description="Calculate Ackermann number for the given inputs",
    tags=["algorithms"],
    operation_id="calculateAckermann",
    response_model=int,
    status_code=200,
)
def handle_ackermann(m: int, n: int) -> Optional[int]:
    if n < 0 or m < 0:
        raise HTTPException(
            status_code=422, detail=f"Can't calculate Ackermann number for negative integers."
        )

    try:
        return ackermann(int(m), int(n))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Something went wrong while calculateing Ackermann of {m} {n}"
        ) from e


@router.get(
    "/algorithms/factorial",
    name="Calculate factorial number",
    description="Calculate factorial of the given non negative integer",
    tags=["algorithms"],
    operation_id="calculateFactorial",
    response_model=int,
    status_code=200,
)
def handle_factorial(n: int) -> Optional[int]:
    if n < 0:
        raise HTTPException(
            status_code=422, detail=f"Can't calculate factorial for a negative integers."
        )

    try:
        return factorial(int(n))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Something went wrong while calculateing factorial of {n}"
        ) from e
