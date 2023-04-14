import requests


def callback_request(pg_url, order_number, md_order):
    callback_url = f"{pg_url}/api/v1/sberbank?orderNumber={order_number[0]}&mdOrder={md_order}&operation=deposited&status=1"
    callback_response = requests.get(callback_url)
    assert callback_response.status_code == 200


def callback_refund_request(pg_url, order_number, md_order, order_item_sum):
    refund_amount = round(order_item_sum * 100)
    callback_refund_url = f"{pg_url}/api/v1/sberbank?orderNumber={order_number[0]}&mdOrder={md_order}&operation=refunded&status=1&refundAmount={refund_amount}"
    callback_refund_response = requests.get(callback_refund_url)
    assert callback_refund_response.status_code == 200