FROM python:3.12

WORKDIR /app

COPY . .
COPY ./fastapi-application/.env .
COPY ./fastapi-application/.env.template .

RUN pip install --no-cache-dir uv==0.6.1

RUN uv sync

CMD ["/app/.venv/bin/python", "./fastapi-application/run"]
