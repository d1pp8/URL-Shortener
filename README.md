# URL Shortener

> ⚠️ **Learning project.** I'm learning FastAPI, so this code is not intended for production use.

A simple URL shortener service built with FastAPI.

## Tech stack

- Python 3.13+
- FastAPI + Uvicorn
- PostgreSQL 17 (Docker)
- SQLAlchemy 2 (async) + asyncpg
- Alembic (migrations)
- pydantic-settings

## Getting started

1. Install dependencies (the project uses `pyproject.toml`, for example via [uv](https://docs.astral.sh/uv/)):

   ```bash
   uv sync
   ```

2. Create a `.env` file based on `.env.example` and fill in your values:

   ```bash
   cp .env.example .env
   ```

3. Start the database:

   ```bash
   docker compose up -d
   ```

4. Apply migrations:

   ```bash
   alembic upgrade head
   ```

5. Run the app:

   ```bash
   uvicorn main:app --reload
   ```

API docs (Swagger): http://127.0.0.1:8000/docs

## API

| Method | Path                 | Description                              |
|--------|----------------------|------------------------------------------|
| POST   | `/d-short/short_url` | Create a short link                      |
| GET    | `/d-short/{slug}`    | Redirect to the original URL (302)       |

Example:

```bash
curl -X POST http://127.0.0.1:8000/d-short/short_url \
  -H "Content-Type: application/json" \
  -d '{"long_url": "https://example.com/some/long/path"}'
```

Response:

```json
{"data": "aB3xYz"}
```

After that, `http://127.0.0.1:8000/d-short/aB3xYz` will redirect to the original URL.

## Project structure

```
app/
  api/          # endpoints
  services/     # business logic (slug generation)
  repository/   # database access
db/             # config, connection, models, migrations
main.py         # entry point
```