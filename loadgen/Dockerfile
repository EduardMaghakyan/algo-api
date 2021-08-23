FROM python:3.9.6-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY locustfile.py .

ENTRYPOINT locust --host="http://${FRONTEND_ADDR}" --headless -u "${USERS:-10}" 2>&1
