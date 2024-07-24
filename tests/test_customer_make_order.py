import allure
import requests

from data import ORDERS, STATUS_INGREDIENTS_REQUIRED, STATUS_INVALID_INGREDIENTS


class TestCustomerMakeOrder:
    @allure.title("Тест проверяет создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_ingredients_authorized(self, get_user_token, get_ingredients):
        response = requests.post(ORDERS, headers=get_user_token, json={"ingredients": get_ingredients[:2]})
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Тест проверяет создание заказа без авторизации и с ингредиентами")
    def test_create_order_with_ingredients_unauthorized(self, get_ingredients):
        response = requests.post(ORDERS, json={"ingredients": get_ingredients[:2]})
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Тест проверяет создание заказа с авторизацией и без ингредиентов")
    def test_create_order_without_ingredients_authorized(self, get_user_token):
        response = requests.post(ORDERS, headers=get_user_token, json={"ingredients": []})
        assert response.status_code == 400 and response.json()["message"] == STATUS_INGREDIENTS_REQUIRED

    @allure.title("Тест проверяет создание заказа без авторизации и без ингредиентов")
    def test_create_order_without_ingredients_unauthorized(self):
        response = requests.post(ORDERS)
        assert response.status_code == 400 and response.json()["message"] == STATUS_INGREDIENTS_REQUIRED

    @allure.title("Тест проверяет создание заказа с невалидными ингредиентами")
    def test_create_order_with_invalid_ingredient_hash(self, get_user_token):
        response = requests.post(ORDERS, headers=get_user_token, json={"ingredients": ["invalid_hash"]})
        assert response.status_code == 400 and response.json()["message"] == STATUS_INVALID_INGREDIENTS
