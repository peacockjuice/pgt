import requests
import json

def setup_mockserver():
    headers = {'Content-Type': 'application/json'}

    data = {
        "httpRequest": {
            "method": "POST",
            "path": "/payment/rest/register.do"
        },
        "httpResponse": {
            "statusCode": 200,
            "body": json.dumps({
                "orderId": "12345",
                "formUrl": "http://mock-payment-gateway"
            })
        }
    }

    response = requests.post('http://localhost:1080/mockserver/expectation', headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        print("MockServer expectation created successfully")
    else:
        print("Failed to create MockServer expectation")

if __name__ == "__main__":
    setup_mockserver()
