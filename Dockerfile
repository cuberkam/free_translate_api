FROM python:3.10-slim-bookworm

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1 \ PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY requirements.txt .
RUN uv pip install -r requirements.txt --system

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "core.wsgi:application"]
