from flask import Flask, request, jsonify
from urllib.parse import urlparse, parse_qs


app = Flask(__name__)

import logging
logging.basicConfig(level=logging.DEBUG)

@app.route("/payment/rest/getOrderStatusExtended.do", methods=["POST"])
def get_order_status_extended():
    # Получение входящих данных из запроса
    user_name = request.form.get("userName")
    password = request.form.get("password")
    order_number = request.form.get("orderNumber")
    language = request.form.get("language")

    # Здесь вы можете добавить логику проверки и обработки полученных данных, если это необходимо

    # Создание симулированного ответа
    response_data = {
        "errorCode": "0",
        "errorMessage": "Успешно",
        "orderStatus": 2,
        "orderNumber": order_number,
        # Здесь добавьте дополнительные поля, которые должны присутствовать в ответе
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

    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
