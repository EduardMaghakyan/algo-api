from fastapi import APIRouter

from .routes import algorithms

router = APIRouter()


router.include_router(algorithms.router)
