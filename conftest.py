import random
import string

import pytest
import requests

from data import USER_LOGIN, USER_UPDATE, GET_INGREDIENTS, USER_SIGN_UP


@pytest.fixture(scope='function')
def generate_user_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def generate_random_email():
        random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f'{random_part}@test.com'

    email = generate_random_email()
    password = generate_random_string(10)
    name = generate_random_string(10)

    return {
        "email": email,
        "password": password,
        "name": name
    }


@pytest.fixture(scope='function')
def create_new_customer_and_delete_after_test(generate_user_data):
    email = generate_user_data["email"]
    password = generate_user_data["password"]
    name = generate_user_data["name"]

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    yield payload

    response = requests.post(USER_LOGIN, json={"email": email, "password": password})
    if response.status_code == 200 and 'accessToken' in response.json():
        token = response.json()['accessToken']
        requests.delete(
            USER_UPDATE,
            json={"user": {"email": email, "name": name}},
            headers={'Authorization': token}
        )


@pytest.fixture(scope='function')
def get_user_token(generate_user_data):
    email = generate_user_data["email"]
    password = generate_user_data["password"]
    name = generate_user_data["name"]

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    requests.post(USER_SIGN_UP, json=payload)

    response = requests.post(USER_LOGIN, json={"email": payload['email'], "password": payload['password']})
    token = response.json().get('accessToken')
    yield {"Authorization": token}

    if response.status_code == 200 and 'accessToken' in response.json():
        token = response.json()['accessToken']
        requests.delete(
            USER_UPDATE,
            json={"user": {"email": email, "name": name}},
            headers={'Authorization': token}
        )


@pytest.fixture(scope='function')
def get_ingredients():
    response = requests.get(GET_INGREDIENTS)
    data = response.json().get('data')
    return [ingredient["_id"] for ingredient in data]
