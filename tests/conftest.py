import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient
from typing import Any, Generator
from app.api.v1.endpoints import emails


def start_application():
    app = FastAPI()
    app.include_router(emails.router)
    return app


@pytest.fixture(autouse=True)
def app() -> Generator[FastAPI, Any, None]:
    """
    Create an application
    """
    _app = start_application()

    yield _app


@pytest.fixture(scope="function")
def client(
    app: FastAPI
) -> Generator[TestClient, Any, None]:
    """
    Create a client
    """

    with TestClient(app) as client:
        yield client