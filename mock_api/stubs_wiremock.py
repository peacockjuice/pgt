import requests
import json
import uuid

mock_server_url = "http://x.x.x.x:1080"
registerDo_endpoint = "/payment/rest/register.do"
getOrderStatusExtendedDo_endpoint = "/payment/rest/getOrderStatusExtended.do"

def create_registerDo_stub():
    order_id = str(uuid.uuid4())

    stub = {
        "request": {
            "method": "POST",
            "url": registerDo_endpoint
        },
        "response": {
            "status": 200,
            "body": json.dumps({
                "orderId": order_id,
                "formUrl": f"http://mock:1080/payment/merchants/sbersafe_sberid/payment_ru.html?mdOrder={order_id}"
            })
        }
    }

    response = requests.post(f"{mock_server_url}/__admin/mappings", json=stub)

    if response.status_code == 201:
        print(f"Stub created with generated orderId and formUrl")
    else:
        print(f"Failed to create stub: {response.status_code}, {response.text}")


def create_getOrderStatusExtendedDo_stub(order_id, order_status):

    stub = {
        "request": {
            "method": "POST",
            "url": getOrderStatusExtendedDo_endpoint,
            "bodyPatterns": [
                {
                    "matches": f"orderId={order_id}&password=yarcheplus&userName=yarcheplus-api"
                }
            ]
        },
        "response": {
            "status": 200,
            "headers": {
                "Content-Type": "application/json; charset=utf-8"
            },
            "body": json.dumps({
                "errorCode": "0",
                "errorMessage": "Успешно",
                "orderStatus": order_status,
                "orderNumber": order_id,
            }, ensure_ascii=False)
        }
    }

    response = requests.post(f"{mock_server_url}/__admin/mappings", json=stub)

    if response.status_code == 201:
        print(f"Stub created for orderId: {order_id} with orderStatus: {order_status}")
    else:
        print(f"Failed to create stub: {response.status_code}, {response.text}")


def create_getOrderStatusExtendedDo_default_stub():

    stub = {
        "request": {
            "method": "POST",
            "url": getOrderStatusExtendedDo_endpoint,
        },
        "response": {
            "status": 200,
            "body": json.dumps({
                "errorCode": "0",
                "errorMessage": "Успешно_Default",
                "orderStatus": 2,
            })
        }
    }

    response = requests.post(f"{mock_server_url}/__admin/mappings", json=stub)

    if response.status_code == 201:
        print("Default stub created successfully.")
    else:
        print(f"Failed to create default stub: {response.status_code}, {response.text}")


def mockServer_stub_tearDown():
    response = requests.delete(f"{mock_server_url}/__admin/mappings")

    if response.status_code == 200:
        print("All stubs deleted successfully.")
    else:
        print(f"Failed to delete stubs: {response.status_code}, {response.text}")
