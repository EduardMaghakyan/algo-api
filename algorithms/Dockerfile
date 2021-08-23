FROM python:3.9.6-slim

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml ./

COPY ./src /app/

RUN poetry install

EXPOSE 8000

ENTRYPOINT ["poetry", "run"]
CMD ["uvicorn", "algo_api.interface.api.main:app" , "--host", "0.0.0.0"]
