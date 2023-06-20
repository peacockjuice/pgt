import pytest
from config.config import BMP_API_URL, BMP_API_TOKEN, BMP_API_TOKEN_ADMIN, PG_URL
from constants.common import order_status_completed
from constants.route import bmp_api_url_graphql

# Функции для подготовки и выполнения тестовых запросов
from core.bmp_gql_input import create_order_variables, delivery_slots_variables, update_products_in_cart_variables
from core.test_utils import get_order_info_from_pg_db, check_order_response, get_random_delivery_token
from core.pg_callbacks import callback_request, callback_refund_request
from core.bmp_gql import send_graphql_request
from core.bmp_rest_query import update_order_data, change_order_status
from core.bmp_gql_query import create_order, delivery_slots, update_products_in_cart

# Дата провайдер
delivery_address_id = 1579839
order_sum = 2327.95
products_and_amounts = [(4328, 202), (2574, 1)]
update_products_in_cart_input = update_products_in_cart_variables(products_and_amounts)
send_graphql_request(update_products_in_cart, update_products_in_cart_input, BMP_API_TOKEN, bmp_api_url_graphql)
delivery_slots_input = delivery_slots_variables(delivery_address_id, products_and_amounts, order_sum)
delivery_slots_response = send_graphql_request(delivery_slots, delivery_slots_input, BMP_API_TOKEN, bmp_api_url_graphql)
delivery_token = get_random_delivery_token(delivery_slots_response)
create_order_input = create_order_variables(delivery_token, products_and_amounts)


@pytest.mark.parametrize("bmp_api_url, bmp_api_token, bmp_api_token_admin", [
    (BMP_API_URL, BMP_API_TOKEN, BMP_API_TOKEN_ADMIN)
])
def test_create_order(bmp_api_url, bmp_api_token, bmp_api_token_admin):
    # Отправляем запрос на создание заказа и проверяем ответ на создание заказа
    create_order_response = send_graphql_request(create_order, create_order_input, bmp_api_token, bmp_api_url_graphql)
    order_data, order_id, order_sum, order_item_id, order_item_sum, vendor_form_url, md_order = check_order_response(create_order_response)

    # Получаем информацию о заказе из БД ПШ (order_number мб оптимальнее получить из инпута в /payment/rest/register.do)
    payment_id, order_number = get_order_info_from_pg_db(md_order)

    # Отправляем коллбэк на подтверждение оплаты заказа
    callback_request(PG_URL, order_number, md_order)

    # Обновляем данные заказа через REST (вычерк позиции из заказа)
    update_order_data(bmp_api_url, bmp_api_token_admin, order_id, order_sum, order_item_id, order_item_sum)

    # Изменяем статус заказа на "completed"
    change_order_status(bmp_api_url, bmp_api_token_admin, order_id, order_status_completed)

    # Отправляем коллбэк на возврат средств
    callback_refund_request(PG_URL, order_number, md_order, order_item_sum)
