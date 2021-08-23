from fastapi.testclient import TestClient

from algo_api.interface.api.main import app

client = TestClient(app)


def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"msg": "OK"}


def test_fibonacci_missing_argument():
    response = client.get("/v1/algorithms/fibonacci")
    assert response.status_code == 422


def test_fibonacci_negative_number():
    response = client.get("/v1/algorithms/fibonacci?n=-2")
    response_body = response.json()

    assert response.status_code == 422
    assert response_body["detail"] == "Can't calculate Fibonacci number for negative integers."


def test_fibonacci_ok():
    response = client.get("/v1/algorithms/fibonacci?n=52")
    response_body = response.json()

    assert response.status_code == 200
    assert response_body == 32951280099
