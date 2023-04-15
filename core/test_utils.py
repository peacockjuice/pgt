import uuid
import psycopg2
from typing import Dict, Any
from random import choice
from config.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


# check_order_response тут временно и это надо в другое место, 100%
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


def connect_to_db():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn


def get_order_info_from_db(md_order):
    with connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM payment WHERE bank_id = %s", (md_order,))
            payment_id = cursor.fetchone()

            cursor.execute("SELECT number FROM \"order\" WHERE payment_id = %s", (payment_id,))
            order_number = cursor.fetchone()
    return payment_id, order_number


def random_delivery_token(response_data: Dict[str, Any]) -> str:
    delivery_slot_list = response_data["data"]["deliverySlots"]["list"]
    random_delivery_token = choice(delivery_slot_list)
    return random_delivery_token["deliveryToken"]