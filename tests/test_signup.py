def test_signup_creates_user_successfully(client):
    user_data = {
        "name": "teste",
        "email": "teamo@amo.com",
        "phone": "41999999999",
        "date_of_birth": "1988-01-01",
        "password": "amora"
    }

    response = client.post("api/v1/auth/signup", json=user_data)
    assert response.status_code in (200, 201)
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["name"] == user_data["name"]
