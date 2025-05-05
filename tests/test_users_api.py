import pytest
from utils.client_api import Api

import uuid



@pytest.fixture(scope="session")
def api():
    return Api()

def test_getuser_validation(api):
    response = api.get("users")
    print(response.json())
    assert response.status_code == 200
    print(response.status_code)

def test_createuser_validation(api, load_user_data):
    # user_data =  {
    # "name": "Leann",
    # "username": "Bruet",
    # "email": "testing@april.biz"
    # }
    user_data = load_user_data["new_user"]

    unique_email = f"({uuid.uuid4().hex[:8]})@gmail.com"
    print(unique_email)
    user_data["email"] =unique_email
    response = api.post("users", user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()["name"] == "Leann"
    print(response.json()["id"])
    print(response.status_code)

    response = api.get("users/1")
    print(response.json())
    assert response.status_code == 200


def test_udateuser_validation(api):
    user_data =  {
    "name": "Leann prashnt",
    "username": "Bruet",
    "email": "testing@april.biz"
    }
    response = api.put("users/1", user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["name"] == "Leann prashnt"


def test_deleteuser_validation(api):
    response = api.delete("users/1")
    print(response.json())
    assert response.status_code == 200