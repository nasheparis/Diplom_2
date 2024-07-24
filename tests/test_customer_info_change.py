import allure
import pytest
import requests

from data import USER_UPDATE, STATUS_UNAUTHORIZED


class TestCustomerInfoChange:
    @pytest.mark.parametrize("field", ["name", "email", "password"])
    @allure.title("Тест проверяет изменение полей email, password, name с авторизацией")
    def test_customer_info_changed_authorized(self, get_user_token, field, generate_user_data):
        new_value = generate_user_data[field]
        update_data = {field: new_value}
        response = requests.patch(USER_UPDATE, json=update_data, headers=get_user_token)
        assert response.status_code == 200 and response.json()['success'] is True

    @pytest.mark.parametrize("field, new_value", [
        ("name", "Updated Name"),
        ("email", "updated_email@test.com"),
        ("password", "UpdatedPassword123")
    ])
    @allure.title("Тест проверяет изменение полей email, password, name без авторизации")
    def test_customer_info_changed_unauthorized(self, field, new_value):
        update_data = {field: new_value}
        response = requests.patch(USER_UPDATE, json=update_data)
        assert response.status_code == 401 and response.json()['message'] == STATUS_UNAUTHORIZED
