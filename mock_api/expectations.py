import requests
import json
import uuid

mock_server_url = "http://13.50.241.89:1080"
registerDo_endpoint = "/payment/rest/register.do"
getOrderStatusExtendedDo_endpoint = "/payment/rest/getOrderStatusExtended.do"


def create_registerDo_exp():
    order_id = str(uuid.uuid4())

    expectation = {
        "httpRequest": {
            "method": "POST",
            "path": registerDo_endpoint
        },
        "httpResponse": {
            "statusCode": 200,
            "body": json.dumps({
                "orderId": order_id,
                "formUrl": f"http://mock:1080/payment/merchants/sbersafe_sberid/payment_ru.html?mdOrder={order_id}"
            })
        },
        "times": {
            "unlimited": True
        }
    }

    response = requests.put(f"{mock_server_url}/mockserver/expectation", json=expectation)

    if response.status_code == 201:
        print(f"Expectation created with generated orderId and formUrl")
    else:
        print(f"Failed to create expectation: {response.status_code}, {response.text}")


def create_getOrderStatusExtendedDo_exp(order_id, order_status):

    expectation = {
        "httpRequest": {
            "method": "POST",
            "path": getOrderStatusExtendedDo_endpoint,
            "body": {
                "type": "STRING",
                "contentType": "application/x-www-form-urlencoded",
                "string": f"orderId={order_id}&password=yarcheplus&userName=yarcheplus-api"
            }
        },
        "httpResponse": {
            "statusCode": 200,
            "headers": {
                "Content-Type": ["application/json; charset=utf-8"]
            },
            "body": json.dumps({
                "errorCode": "0",
                "errorMessage": "Успешно",
                "orderStatus": order_status,
                "orderNumber": order_id,
            }, ensure_ascii=False)
        },
        "times": {
            "remainingTimes": 1
        }
    }

    response = requests.put(f"{mock_server_url}/mockserver/expectation", json=expectation)

    if response.status_code == 201:
        print(f"Expectation created for orderId: {order_id} with orderStatus: {order_status}")
    else:
        print(f"Failed to create expectation: {response.status_code}, {response.text}")



def create_getOrderStatusExtendedDo_default_exp():

    expectation = {
        "httpRequest": {
            "method": "POST",
            "path": getOrderStatusExtendedDo_endpoint,
        },
        "httpResponse": {
            "statusCode": 200,
            "body": json.dumps({
                "errorCode": "0",
                "errorMessage": "Успешно_Default",
                "orderStatus": 2,
            })
        },
        "times": {
            "unlimited": True
        }
    }

    response = requests.put(f"{mock_server_url}/mockserver/expectation", json=expectation)

    if response.status_code == 201:
        print("Default expectation created successfully.")
    else:
        print(f"Failed to create default expectation: {response.status_code}, {response.text}")


def mockServer_exp_tearDown():
    response = requests.put(f"{mock_server_url}/mockserver/reset")