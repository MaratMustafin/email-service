from app.domains.email import Email
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient



def test_email_create(
    client: TestClient,
):
    email = Email(
        id=1,
        to="you@you.com",
        message="Hello World",
        subject="World"
    )
    req_data = jsonable_encoder(email)

    response = client.post(
        "/send_email",
        json=req_data,
    )
    data = response.json()
    print('data', data)
    assert response.status_code == 201
    assert Email(**data)