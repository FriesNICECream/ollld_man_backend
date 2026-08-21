from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(title=settings.app_name)


@app.get("/health", tags=["system"])
async def health_check() -> dict[str, str]:
    """Confirm that the HTTP application is running."""
    return {"status": "ok"}
