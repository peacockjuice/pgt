import requests
from core.graphql_requests import get_headers
from core.rest_requests import rest_order_items_patch_query, rest_status_patch_query


def update_order_data(bmp_api_url, bmp_api_token_admin, order_id, order_sum, order_item_id, order_item_sum):
    bmp_api_rest_orders = f"{bmp_api_url}/orders/{order_id}"
    headers = get_headers(bmp_api_token_admin)
    query = rest_order_items_patch_query(order_id, order_sum - order_item_sum, order_item_id)
    patch_response = requests.patch(bmp_api_rest_orders, headers=headers, json=query)
    assert patch_response.status_code == 200


def change_order_status(bmp_api_url, bmp_api_token_admin, order_id, new_status):
    bmp_api_rest_orders = f"{bmp_api_url}/orders/{order_id}"
    headers = get_headers(bmp_api_token_admin)
    query = rest_status_patch_query(order_id, new_status)
    status_response = requests.patch(bmp_api_rest_orders, headers=headers, json=query)
    assert status_response.status_code == 200