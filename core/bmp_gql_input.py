from typing import List, Tuple, Dict, Any
from core.test_utils import get_product_ids_list
from constants.common import payment_method_online


def create_order_variables(delivery_token, products: List[Tuple[int, int]]) -> Dict[str, Any]:
    product_ids = get_product_ids_list(products)
    input_products = [{"id": product_id} for product_id in product_ids]

    return {
        "input": {
            "deliveryToken": delivery_token,
            "paymentMethodCode": payment_method_online,
            "firstname": "autotest",
            "lastname": "autotest",
            "phone": "+79998887766",
            "email": "vpavlin@test.com",
            "isAgreementAccepted": True,
            "parts": [{"products": input_products}],
            "clientId": "GA1.5.216541125.1636451600"
        }
    }


def delivery_slots_variables(delivery_address_id, product_ids, order_sum):
    product_ids = get_product_ids_list(product_ids)

    return {
        "input": {
            "deliveryAddressId": delivery_address_id,
            "paymentMethodCodes": ["online", "card"],
            "productIds": product_ids,
            "orderSum": order_sum
            }
    }


def update_products_in_cart_variables(products: List[Tuple[int, int]]) -> Dict[str, Any]:
    input_products = [{"id": product_id, "amount": amount} for product_id, amount in products]

    return {
        "input": {
            "products": input_products
        }
    }