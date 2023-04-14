def rest_order_items_patch_query(order_id, order_sum, order_item_id):
    return {
        "data": {
            "meta": {
                "method": "patch"
            },
            "id": order_id,
            "attributes": {
                "order_sum": order_sum
            },
            "relationships": {
                "order-items": {
                    "data": [
                        {
                            "id": order_item_id,
                            "meta": {
                                "method": "patch"
                            },
                            "attributes": {
                                "is_active": False
                            }
                        }
                    ]
                }
            }
        }
    }


def rest_status_patch_query(order_id, status):
    return {
        "data": {
            "meta": {
                "method": "patch"
            },
            "id": order_id,
            "attributes": {
                "status": status
            }
        }
    }