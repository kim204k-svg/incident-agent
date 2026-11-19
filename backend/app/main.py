from fastapi import FastAPI

from app.config import settings
from app.db import check_db

app = FastAPI(title="incident-agent", version="0.1.0")


@app.get("/health")
def health() -> dict:
    """애플리케이션과 DB 연결 상태를 확인한다."""
    return {"status": "ok", "env": settings.app_env, "db": check_db()}
