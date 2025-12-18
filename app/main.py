from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base

from app.models import user as user_model  # noqa: F401
from app.models import task as task_model  # noqa: F401

from app.routers.auth import router as auth_router
from app.routers.tasks import router as tasks_router

def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME)
    Base.metadata.create_all(bind=engine)

    app.include_router(auth_router)
    app.include_router(tasks_router)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app

app = create_app()
