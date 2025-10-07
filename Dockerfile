ARG VERSION=3.12-slim

FROM python:$VERSION AS base
WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"
RUN pip install --upgrade pip uv
COPY pyproject.toml uv.lock /
COPY . .
RUN uv sync

FROM base AS books
CMD ["uvicorn", "backend.services.books:app", "--host", "0.0.0.0", "--port", "88"]

FROM base AS users
CMD ["uvicorn", "backend.services.auth:app", "--host", "0.0.0.0", "--port", "89"]

FROM base AS auth
CMD ["uvicorn", "backend.services.users:app", "--host", "0.0.0.0", "--port", "90"]
