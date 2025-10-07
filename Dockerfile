ARG VERSION=3.12-slim

FROM python:$VERSION AS base
WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"
RUN pip install --upgrade pip uv
COPY pyproject.toml uv.lock /
COPY . .
RUN uv sync


# final backend stage
FROM base AS books
CMD ["uvicorn", "backend.services.books:app", "--host", "0.0.0.0", "--port", "88"]
