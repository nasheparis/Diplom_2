import allure
import requests

from data import USER_SIGN_UP, USER_LOGIN, STATUS_INVALID


class TestCustomerLogin:
    @allure.title("Тест проверяет успешный логин пользователя")
    def test_existing_customer_login(self, create_new_customer_and_delete_after_test):
        payload = create_new_customer_and_delete_after_test
        requests.post(USER_SIGN_UP, json=payload)
        response = requests.post(USER_LOGIN, json={"email": payload['email'], "password": payload['password']})
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title("Тест проверяет, что нельзя войти в аккаунт без email")
    def test_customer_login_no_email(self, create_new_customer_and_delete_after_test):
        payload = create_new_customer_and_delete_after_test
        requests.post(USER_SIGN_UP, json=payload)
        response = requests.post(USER_LOGIN, json={"password": payload['password']})
        assert response.status_code == 401 and response.json()['message'] == STATUS_INVALID

    @allure.title("Тест проверяет, что нельзя войти в аккаунт без password")
    def test_customer_login_no_password(self, create_new_customer_and_delete_after_test):
        payload = create_new_customer_and_delete_after_test
        requests.post(USER_SIGN_UP, json=payload)
        response = requests.post(USER_LOGIN, json={"email": payload['email']})
        assert response.status_code == 401 and response.json()['message'] == STATUS_INVALID

    @allure.title("Тест проверяет, что нельзя войти в аккаунт без обязательных полей")
    def test_customer_login_no_all_required_fields(self):
        response = requests.post(USER_LOGIN, json={})
        assert response.status_code == 401 and response.json()['message'] == STATUS_INVALID
