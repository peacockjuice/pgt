import os
import logging
import uuid

from config.config import SBERMOCK_API_URL
from flask import Flask, request, jsonify

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
logger = logging.getLogger(__name__)

order_status_calls = {}

@app.route("/payment/rest/register.do", methods=["POST"])
def register_order():
    # Получение входящих данных из запроса (позже будет полезно)
    user_name = request.form.get("userName")
    password = request.form.get("password")
    order_number = request.form.get("orderNumber")
    amount = request.form.get("amount")
    return_url = request.form.get("returnUrl")
    fail_url = request.form.get("failUrl")
    description = request.form.get("description")

    logging.info(f"Received request: {request.form}")

    # Создание симулированного ответа
    orderId = str(uuid.uuid4())
    response_data = {
    "orderId": orderId,
    "formUrl": f"{SBERMOCK_API_URL}/payment/merchants/sbersafe_sberid/payment_ru.html?mdOrder={orderId}",
    }

    logger.debug(f"Sending response: {response_data}")

    # Отправка симулированного ответа
    return jsonify(response_data)

@app.route("/payment/rest/getOrderStatusExtended.do", methods=["POST"])
def get_order_status_extended():
    global order_status_calls

    # Получение входящих данных из запроса
    order_id = request.form.get("orderId")

    logging.info(f"Received request: {request.form}")

    # Далее - уёбский костыль, который отдаёт разные статусы на одном эндпоинте. НЕОБХОДИМО реализовать ИНАЧЕ!
    # Увеличиваем счетчик вызовов для данного orderId
    if order_id in order_status_calls:
        order_status_calls[order_id] += 1
    else:
        order_status_calls[order_id] = 1

    # Определяем статус заказа на основе счетчика вызовов
    if order_status_calls[order_id] == 1:
        order_status = 2
    elif order_status_calls[order_id] == 2:
        order_status = 4
    else:
        order_status = 0  # Дефолт-значение, если будет более двух запросов.

    response_data = {
        "errorCode": "0",
        "errorMessage": "Успешно",
        "orderStatus": order_status,
        "orderNumber": order_id,
    }

    logger.debug(f"Sending response: {response_data}")

    return jsonify(response_data)


@app.route("/payment/rest/refund.do", methods=["POST"])
def refund_order():
    user_name = request.form.get("userName")
    password = request.form.get("password")
    order_id = request.form.get("orderId")
    amount = request.form.get("amount")

    logging.info(f"Received request: {request.form}")

    response_data = {
        "orderNumber": order_id,
        "orderStatus": 4,
        "errorCode": "0",
        "errorMessage": "Успешно",
        "paymentAmountInfo": {
            "approvedAmount": 233291,
            "depositedAmount": 221796,
            "refundedAmount": 11495
        }
    }

    logger.debug(f"Sending response: {response_data}")

    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
