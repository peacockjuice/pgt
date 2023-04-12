import requests
import uuid
from config.database import connect_to_db
from test_data.data import get_headers, rest_order_items_patch_query, rest_status_patch_query

def send_graphql_request(bmp_api_url, bmp_api_token, query, input_data):
    headers_graphql = get_headers(bmp_api_token)
    bmp_api_url_graphql = f"{bmp_api_url}/graphql"
    response = requests.post(bmp_api_url_graphql, headers=headers_graphql, json={"query": query, "variables": input_data})
    response_data = response.json()
    assert response.status_code == 200
    assert "errors" not in response_data
    return response_data

def check_order_response(response_data):
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
    return order_data, order_id, order_sum, order_item_id, order_item_sum, vendor_form_url, md_order

def get_order_info_from_db(md_order):
    with connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM payment WHERE bank_id = %s", (md_order,))
            payment_id = cursor.fetchone()

            cursor.execute("SELECT number FROM \"order\" WHERE payment_id = %s", (payment_id,))
            order_number = cursor.fetchone()
    return payment_id, order_number

def send_callback_request(pg_url, order_number, md_order):
    callback_url = f"{pg_url}/api/v1/sberbank?orderNumber={order_number[0]}&mdOrder={md_order}&operation=deposited&status=1"
    callback_response = requests.get(callback_url)
    assert callback_response.status_code == 200

def update_order_data(bmp_api_url, bmp_api_token_admin, order_id, order_sum, order_item_id, order_item_sum):
    bmp_api_rest_orders = f"{bmp_api_url}/orders/{order_id}"
    headers_rest = get_headers(bmp_api_token_admin)
    rest_query1 = rest_order_items_patch_query(order_id, order_sum - order_item_sum, order_item_id)
    patch_response = requests.patch(bmp_api_rest_orders, headers=headers_rest, json=rest_query1)
    assert patch_response.status_code == 200

def change_order_status(bmp_api_url, bmp_api_token_admin, order_id, new_status):
    bmp_api_rest_orders = f"{bmp_api_url}/orders/{order_id}"
    headers_rest = get_headers(bmp_api_token_admin)
    rest_query2 = rest_status_patch_query(order_id, new_status)
    status_response = requests.patch(bmp_api_rest_orders, headers=headers_rest, json=rest_query2)
    assert status_response.status_code == 200

def send_callback_refund_request(pg_url, order_number, md_order, order_item_sum):
    refund_amount = round(order_item_sum * 100)
    callback_refund_url = f"{pg_url}/api/v1/sberbank?orderNumber={order_number[0]}&mdOrder={md_order}&operation=refunded&status=1&refundAmount={refund_amount}"
    callback_refund_response = requests.get(callback_refund_url)
    assert callback_refund_response.status_code == 200
