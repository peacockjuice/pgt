import pytest
import requests
import uuid

from config.config import BMP_API_URL, BMP_API_TOKEN, BMP_API_TOKEN_ADMIN, PG_URL
from config.database import connect_to_db
from dotenv import load_dotenv
from test_data.data import query, input_data, get_headers, rest_query, rest_status_patch_query

# Загрузка переменных окружения из файла .env
load_dotenv()

@pytest.mark.parametrize("bmp_api_url, bmp_api_token, bmp_api_token_admin, query, input_data", [
    (BMP_API_URL, BMP_API_TOKEN, BMP_API_TOKEN_ADMIN, query, input_data)
])
def test_create_order(bmp_api_url, bmp_api_token, bmp_api_token_admin, query, input_data):
    print("Запуск test_create_order")
    headers_graphql = get_headers(bmp_api_token)
    bmp_api_url_graphql = f"{bmp_api_url}/graphql"

    response = requests.post(bmp_api_url_graphql, headers=headers_graphql, json={"query": query, "variables": input_data})
    response_data = response.json()

    assert response.status_code == 200
    assert "errors" not in response_data

    order_data = response_data["data"]["createOrder"]
    order_id = order_data["orders"][0]["id"]
    order_sum = order_data["orders"][0]["orderSum"]

    order_item_id = order_data["orders"][0]["orderItems"][0]["id"]
    order_item_sum = order_data["orders"][0]["orderItems"][0]["orderItemSum"]
    order_sum_after_vicherk = order_sum - order_item_sum

    vendor_form_url = order_data["orders"][0]["paymentDetail"]["paymentPartList"][0]["vendorFormUrl"]
    md_order = vendor_form_url.split('=')[1]
    md_order_uuid = uuid.UUID(md_order)
    assert order_id is not None
    assert md_order_uuid is not None

    # Подключение к БД PG и выполнение SQL-запросов
    with connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM payment WHERE bank_id = %s", (md_order,))
            payment_id = cursor.fetchone()

            cursor.execute("SELECT number FROM \"order\" WHERE payment_id = %s", (payment_id,))
            order_number = cursor.fetchone()

    # Отправка коллбэк-запроса на URL PG
    callback_url = f"{PG_URL}/api/v1/sberbank?orderNumber={order_number[0]}&mdOrder={md_order}&operation=deposited&status=1"
    callback_response = requests.get(callback_url)
    assert callback_response.status_code == 200

    bmp_api_rest_orders = f"{bmp_api_url}/orders/{order_id}"
    headers_rest = get_headers(bmp_api_token_admin)
    rest_query1 = rest_query(order_id, order_sum_after_vicherk, order_item_id)
    patch_response = requests.patch(bmp_api_rest_orders, headers=headers_rest, json=rest_query1)

    assert patch_response.status_code == 200

    rest_query2 = rest_status_patch_query(order_id, "completed")
    status_response = requests.patch(bmp_api_rest_orders, headers=headers_rest, json=rest_query2)

    assert status_response.status_code == 200

    refund_amount = round(order_item_sum * 100)
    callback_refund_url = f"{PG_URL}/api/v1/sberbank?orderNumber={order_number[0]}&mdOrder={md_order}&operation=refunded&status=1&refundAmount={refund_amount}"
    callback_refund_response = requests.get(callback_refund_url)
    assert callback_refund_response.status_code == 200

    assert status_response.status_code == 200


