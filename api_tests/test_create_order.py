import requests
import pytest
import uuid
from urllib.parse import urlencode
from dotenv import load_dotenv
from test_data.test_data import query, input_data, get_headers
from config import BMP_API_URL, BMP_API_TOKEN, PG_URL, SBERBANK_MOCK_API_URL
from database import connect_to_db

# Загрузка переменных окружения из файла .env
load_dotenv()

@pytest.mark.parametrize("bmp_api_url, bmp_api_token, query, input_data", [
    (BMP_API_URL, BMP_API_TOKEN, query, input_data)
])
def test_create_order(bmp_api_url, bmp_api_token, query, input_data):
    print("Запуск функции test_create_order")
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

    # Подключение к базе данных и выполнение SQL-запросов
    with connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM payment WHERE bank_id = %s", (md_order,))
            payment_id = cursor.fetchone()

            cursor.execute("SELECT number FROM \"order\" WHERE payment_id = %s", (payment_id,))
            order_number = cursor.fetchone()

    # Отправка запроса на псевдо-API Сбербанка getOrderStatusExtended.do
    sberbank_request_data = {
        "userName": "X",
        "password": "X",
        "orderNumber": order_number[0],
        "language": "ru"
    }
    sberbank_request_headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    sberbank_request_url = SBERBANK_MOCK_API_URL

    sberbank_request_response = requests.post(sberbank_request_url, data=urlencode(sberbank_request_data), headers=sberbank_request_headers)
    print("Значение sberbank_request_response:", sberbank_request_response)
    sberbank_request_response_data = sberbank_request_response.json()
    print("Значение sberbank_request_response_data:", sberbank_request_response_data)

    #Отправка коллбэк-запроса на URL стенда PG
    callback_url = f"{PG_URL}/api/v1/sberbank?orderNumber={order_number[0]}&mdOrder={md_order}&operation=deposited&status=1"
    callback_response = requests.get(callback_url)
    assert callback_response.status_code == 200