import allure
import requests

from data import USER_SIGN_UP, STATUS_ALREADY_EXISTS, STATUS_FORBIDDEN


class TestCustomerSignUp:
    @allure.title("Тест проверяет успешую регистрацию пользователя")
    def test_customer_sign_up_positive(self, create_new_customer_and_delete_after_test):
        response = requests.post(USER_SIGN_UP, json=create_new_customer_and_delete_after_test)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title("Тест проверяет регистрацию пользователя, который уже существует")
    def test_customer_sign_up_already_exists(self, create_new_customer_and_delete_after_test):
        requests.post(USER_SIGN_UP, json=create_new_customer_and_delete_after_test)
        response = requests.post(USER_SIGN_UP, json=create_new_customer_and_delete_after_test)
        assert response.status_code == 403 and response.json()['message'] == STATUS_ALREADY_EXISTS

    @allure.title("Тест проверяет, что нельзя зарегистрироваться без email")
    def test_customer_sign_up_no_email(self, create_new_customer_and_delete_after_test):
        payload = create_new_customer_and_delete_after_test.copy()
        payload.pop('email', None)
        response = requests.post(USER_SIGN_UP, json=payload)
        assert response.status_code == 403 and response.json()['message'] == STATUS_FORBIDDEN

    @allure.title("Тест проверяет, что нельзя зарегистрироваться без password")
    def test_customer_sign_up_no_password(self, create_new_customer_and_delete_after_test):
        payload = create_new_customer_and_delete_after_test.copy()
        payload.pop('password', None)
        response = requests.post(USER_SIGN_UP, json=payload)
        assert response.status_code == 403 and response.json()['message'] == STATUS_FORBIDDEN

    @allure.title("Тест проверяет, что нельзя зарегистрироваться без name")
    def test_customer_sign_up_no_name(self, create_new_customer_and_delete_after_test):
        payload = create_new_customer_and_delete_after_test.copy()
        payload.pop('name', None)
        response = requests.post(USER_SIGN_UP, json=payload)
        assert response.status_code == 403 and response.json()['message'] == STATUS_FORBIDDEN

    @allure.title("Тест проверяет, что нельзя зарегистрироваться без обязательных полей")
    def test_customer_sign_up_no_all_required_fields(self, create_new_customer_and_delete_after_test):
        payload = create_new_customer_and_delete_after_test.copy()
        payload.pop('email', None)
        payload.pop('password', None)
        payload.pop('name', None)
        response = requests.post(USER_SIGN_UP, json=payload)
        assert response.status_code == 403 and response.json()['message'] == STATUS_FORBIDDEN
