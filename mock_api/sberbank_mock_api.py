import os
import logging
import uuid

from config import SBERMOCK_API_URL
from flask import Flask, request, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route("/payment/rest/register.do", methods=["POST"])
def register_order():
    # Получение входящих данных из запроса
    user_name = request.form.get("userName")
    password = request.form.get("password")
    order_number = request.form.get("orderNumber")
    amount = request.form.get("amount")
    return_url = request.form.get("returnUrl")
    fail_url = request.form.get("failUrl")
    description = request.form.get("description")

    # Создание симулированного ответа
    orderId = str(uuid.uuid4())
    response_data = {
    "orderId": orderId,
    "formUrl": f"{SBERMOCK_API_URL}/payment/merchants/sbersafe_sberid/payment_ru.html?mdOrder={orderId}",
    }

    # Отправка симулированного ответа
    return jsonify(response_data)

@app.route("/payment/rest/getOrderStatusExtended.do", methods=["POST"])
def get_order_status_extended():
    # Получение входящих данных из запроса
    user_name = request.form.get("userName")
    password = request.form.get("password")
    order_number = request.form.get("orderNumber")
    language = request.form.get("language")

    # Создание симулированного ответа
    response_data = {
        "errorCode": "0",
        "errorMessage": "Успешно",
        "orderStatus": 2,
        "orderNumber": order_number,
    }

    # Отправка симулированного ответа
    return jsonify(response_data)

@app.route("/api/v1/sberbank", methods=["GET"])
def simulate_sberbank_request():
    order_number = request.args.get("orderNumber")
    md_order = request.args.get("mdOrder")
    operation = request.args.get("operation")
    status = request.args.get("status")

    if not all([order_number, md_order, operation, status]):
        return jsonify({"error": "Invalid request parameters"}), 400

    response_data = {
        "orderNumber": order_number,
        "mdOrder": md_order,
        "operation": operation,
        "status": status,
    }

    # Отправка симулированного ответа
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
