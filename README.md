# Diplom_2

Тесты в test_customer_info_change:

- test_customer_info_changed_authorized - Тест проверяет изменение полей email, password, name с авторизацией
- test_customer_info_changed_unauthorized - Тест проверяет изменение полей email, password, name без авторизации

Тесты в test_customer_login:

- test_existing_customer_login - Тест проверяет успешный логин пользователя
- test_customer_login_no_email - Тест проверяет, что нельзя войти в аккаунт без email
- test_customer_login_no_password - Тест проверяет, что нельзя войти в аккаунт без password
- test_customer_login_no_all_required_fields - Тест проверяет, что нельзя войти в аккаунт без обязательных полей

Тесты в test_customer_make_order:

- test_create_order_with_ingredients_authorized - Тест проверяет создание заказа с авторизацией и ингредиентами
- test_create_order_with_ingredients_unauthorized - Тест проверяет создание заказа без авторизации и с ингредиентами
- test_create_order_without_ingredients_authorized - Тест проверяет создание заказа с авторизацией и без ингредиентов
- test_create_order_without_ingredients_unauthorized - Тест проверяет создание заказа без авторизации и без ингредиентов
- test_create_order_with_invalid_ingredient_hash - Тест проверяет создание заказа с невалидными ингредиентами

Тесты в test_customer_orders:

- test_get_customer_orders_authorized - Тест проверяет получение заказов конкретного пользователя с авторизацией
- test_get_customer_orders_unauthorized - Тест проверяет получение заказов конкретного пользователя без авторизации

Тесты в test_customer_sign_up:

- test_customer_sign_up_positive - Тест проверяет успешую регистрацию пользователя
- test_customer_sign_up_already_exists - Тест проверяет регистрацию пользователя, который уже существует
- test_customer_sign_up_no_email - Тест проверяет, что нельзя зарегистрироваться без email
- test_customer_sign_up_no_password - Тест проверяет, что нельзя зарегистрироваться без password
- test_customer_sign_up_no_name - Тест проверяет, что нельзя зарегистрироваться без name
- test_customer_sign_up_no_all_required_fields - Тест проверяет, что нельзя зарегистрироваться без обязательных полей
