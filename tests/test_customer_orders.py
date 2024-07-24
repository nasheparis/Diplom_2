import allure
import requests

from data import ORDERS, STATUS_UNAUTHORIZED


class TestCustomerOrders:
    @allure.title("Тест проверяет получение заказов конкретного пользователя с авторизацией")
    def test_get_customer_orders_authorized(self, get_user_token):
        response = requests.get(ORDERS, headers=get_user_token)
        assert response.status_code == 200 and "orders" in response.json()

    @allure.title("Тест проверяет получение заказов конкретного пользователя без авторизации")
    def test_get_customer_orders_unauthorized(self):
        response = requests.get(ORDERS)
        assert response.status_code == 401 and response.json().get("message") == STATUS_UNAUTHORIZED
