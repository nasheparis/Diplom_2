MAIN_URL = "https://stellarburgers.nomoreparties.site/api"

USER_SIGN_UP = f"{MAIN_URL}/auth/register"
USER_LOGIN = f"{MAIN_URL}/auth/login"
USER_UPDATE = f"{MAIN_URL}/auth/user"
ORDERS = f"{MAIN_URL}/orders"
GET_INGREDIENTS = f"{MAIN_URL}/ingredients"

STATUS_ALREADY_EXISTS = 'User already exists'
STATUS_FORBIDDEN = 'Email, password and name are required fields'
STATUS_INVALID = 'email or password are incorrect'
STATUS_UNAUTHORIZED = 'You should be authorised'
STATUS_INGREDIENTS_REQUIRED = 'Ingredient ids must be provided'
STATUS_INVALID_INGREDIENTS = 'One or more ids provided are incorrect'
