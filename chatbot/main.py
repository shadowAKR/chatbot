"""
Starting point of the FastAPI application
Returns:
    a FastAPI object
"""
from fastapi import FastAPI
from chatbot.core.config import settings
from api.router import api_router

def create_app() -> FastAPI:
    """method to create fastapi application

    Returns:
        FastAPI: return a FastAPI object
    """
    application = FastAPI(title=settings.app_name)
    application.include_router(router=api_router)
    return application

app: FastAPI = create_app()

@app.get("/health")
def health() -> dict[str, str]:
    """
    health check API
    """
    return {"status": "ok"}
