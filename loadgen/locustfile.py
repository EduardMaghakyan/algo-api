import random
from locust import HttpUser, TaskSet, between

def docs(l):
    l.client.get("/docs")

def factorial(l):
    l.client.get(f"/v1/algorithms/factorial?n={random.randint(1, 150)}")

def fibonacci(l):
    l.client.get(f"/v1/algorithms/fibonacci?n={random.randint(1, 150)}")

def ackermann(l):
    l.client.get(f"/v1/algorithms/ackermann?m={random.randint(1, 2)}&n={random.randint(1, 5)}")

def healthcheck(l):
    l.client.get(f"/healthcheck")

class UserBehavior(TaskSet):

    def on_start(self):
        docs(self)

    tasks = {docs: 1,
        ackermann: 2,
        fibonacci: 10,
        factorial: 2
        }

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 10)
