import requests


def test_get_users():
    url = "http://127.0.0.1:5500/"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_user():
    url = "http://127.0.0.1:5500/create_user"
    payload = {"email": "honkrm@gmail.com", "name": "Hon Krm"}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201
    assert response.json() == {"status": "usser added successfully"}
