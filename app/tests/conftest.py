# import asyncio
# from typing import Any, Generator, AsyncGenerator
# import pytest_asyncio

import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # this is where the testing happens


# @pytest.fixture(autouse=True, scope="session")
# def run_migrations() -> None:
#     import os
#
#     print("running migrations..")
#     os.system("alembic upgrade head")
#     yield
#     os.system("alembic downgrade base")


# @pytest.fixture(scope="session")
# def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()
#
#
# @pytest_asyncio.fixture
# async def client() -> AsyncGenerator[TestClient, None]:
#     host, port = "127.0.0.1", "9000"
#     scope = {"client": (host, port)}
#
#     async with TestClient(app, scope=scope) as client:
#         yield client