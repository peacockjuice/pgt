import pytest
import requests
import uuid
from test_data.data import query, input_data
from config.config import BMP_API_URL, BMP_API_TOKEN, BMP_API_TOKEN_ADMIN, PG_URL
from config.database import connect_to_db

# Функции для подготовки и выполнения тестовых запросов
from core.test_utils import (
    send_graphql_request,
    update_order_data,
    send_callback_request,
    send_callback_refund_request, get_order_info_from_db, check_order_response, change_order_status
)

@pytest.mark.parametrize("bmp_api_url, bmp_api_token, bmp_api_token_admin, query, input_data", [
    (BMP_API_URL, BMP_API_TOKEN, BMP_API_TOKEN_ADMIN, query, input_data)
])
def test_create_order(bmp_api_url, bmp_api_token, bmp_api_token_admin, query, input_data):
    # Отправляем запрос на создание заказа и проверяем ответ на создание заказа
    response_data = send_graphql_request(bmp_api_url, bmp_api_token, query, input_data)
    order_data, order_id, order_sum, order_item_id, order_item_sum, vendor_form_url, md_order = check_order_response(response_data)

    # Получаем информацию о заказе из БД (order_number мб оптимальнее получить из инпута приходящих в /payment/rest/register.do)
    payment_id, order_number = get_order_info_from_db(md_order)

    # Отправляем коллбэк на подтверждение оплаты заказа
    send_callback_request(PG_URL, order_number, md_order)

    # Обновляем данные заказа через REST (вычерк позиции из заказа)
    update_order_data(bmp_api_url, bmp_api_token_admin, order_id, order_sum, order_item_id, order_item_sum)

    # Изменяем статус заказа на "completed"
    change_order_status(bmp_api_url, bmp_api_token_admin, order_id, "completed")

    # Отправляем коллбэк на возврат средств
    send_callback_refund_request(PG_URL, order_number, md_order, order_item_sum)
