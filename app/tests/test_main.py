from fastapi.testclient import TestClient
from fastapi import status


def test_main(test_app: TestClient) -> None:
    response = test_app.get("/")
    # resp = await client.get("/")#

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "Hello World"}
