import pytest
import requests
import uuid

from config import BMP_API_URL, BMP_API_TOKEN, PG_URL
from database import connect_to_db
from dotenv import load_dotenv
from test_data.test_data import query, input_data, get_headers

# Загрузка переменных окружения из файла .env
load_dotenv()

@pytest.mark.parametrize("bmp_api_url, bmp_api_token, query, input_data", [
    (BMP_API_URL, BMP_API_TOKEN, query, input_data)
])
def test_create_order(bmp_api_url, bmp_api_token, query, input_data):
    print("Запуск test_create_order")
    headers = get_headers(bmp_api_token)

    response = requests.post(bmp_api_url, headers=headers, json={"query": query, "variables": input_data})
    response_data = response.json()

    assert response.status_code == 200
    assert "errors" not in response_data

    order_data = response_data["data"]["createOrder"]
    order_id = order_data["id"]
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

    #Отправка коллбэк-запроса на URL PG
    callback_url = f"{PG_URL}/api/v1/sberbank?orderNumber={order_number[0]}&mdOrder={md_order}&operation=deposited&status=1"
    callback_response = requests.get(callback_url)
    assert callback_response.status_code == 200