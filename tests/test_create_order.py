import pytest
from config.config import BMP_API_URL, BMP_API_TOKEN, BMP_API_TOKEN_ADMIN, PG_URL

# Функции для подготовки и выполнения тестовых запросов
from test_data.data import create_order_input, delivery_slots_input, update_products_in_cart_input
from core.test_utils import get_order_info_from_db, check_order_response, random_delivery_token
from core.pg_requests import callback_request, callback_refund_request
from core.graphql_requests import send_graphql_request
from core.bmp_requests_rest import update_order_data, change_order_status
from core.bmp_requests_graphql import create_order, delivery_slots, update_products_in_cart


@pytest.mark.parametrize("bmp_api_url, bmp_api_token, bmp_api_token_admin", [
    (BMP_API_URL, BMP_API_TOKEN, BMP_API_TOKEN_ADMIN)
])
def test_create_order(bmp_api_url, bmp_api_token, bmp_api_token_admin):

    # Подготовка перед непосредственной отправкой запроса из БМП, в котором идёт взаимодействие с ПШ/банком
    delivery_address_id = 1579839
    order_sum = 2332.91
    products_and_amount_to_add = [(4328, 202), (3253, 1)]
    product_ids = [product_id for product_id, _ in products_and_amount_to_add]
    update_products_in_cart_input_filled = update_products_in_cart_input(products_and_amount_to_add)
    update_products_in_cart_data = send_graphql_request(bmp_api_url, bmp_api_token, update_products_in_cart, update_products_in_cart_input_filled)
    delivery_slots_input_filled = delivery_slots_input(delivery_address_id, product_ids, order_sum)
    delivery_slots_data = send_graphql_request(bmp_api_url, bmp_api_token, delivery_slots, delivery_slots_input_filled)
    delivery_token = random_delivery_token(delivery_slots_data)
    create_order_input_filled = create_order_input(delivery_token, product_ids)

    # Отправляем запрос на создание заказа и проверяем ответ на создание заказа
    create_order_data = send_graphql_request(bmp_api_url, bmp_api_token, create_order, create_order_input_filled)
    order_data, order_id, order_sum, order_item_id, order_item_sum, vendor_form_url, md_order = check_order_response(create_order_data)

    # Получаем информацию о заказе из БД (order_number мб оптимальнее получить из инпута в /payment/rest/register.do)
    payment_id, order_number = get_order_info_from_db(md_order)

    # Отправляем коллбэк на подтверждение оплаты заказа
    callback_request(PG_URL, order_number, md_order)

    # Обновляем данные заказа через REST (вычерк позиции из заказа)
    update_order_data(bmp_api_url, bmp_api_token_admin, order_id, order_sum, order_item_id, order_item_sum)

    # Изменяем статус заказа на "completed"
    change_order_status(bmp_api_url, bmp_api_token_admin, order_id, "completed")

    # Отправляем коллбэк на возврат средств
    callback_refund_request(PG_URL, order_number, md_order, order_item_sum)
