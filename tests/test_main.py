from fastapi.testclient import TestClient
import pytest
from fastapi import status

from ..app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_register(client: TestClient) -> None:
    response = client.get("/")
    # resp = await client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "Hello World"}
 