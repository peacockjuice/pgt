
# Запрос GraphQL
query = """
mutation ($input: CreateOrderInput!) {
  createOrder(input: $input) {
    id
    number
    groupStatusCode: statusCode
    statusTitle
    dateCreated
    orderGroupSum
    originalOrderGroupSum
    invoiceUrl
    isMy
    isAwaitingCancellation
    isCancellable
    isRepeatable
    hasDebt
    orders {
      id
      number
      statusCode
      statusTitle
      paymentDetail {
        isComplete
        paymentPartList {
          vendorFormUrl
          lifetime
        }
      }
      paymentMethodCode
      paymentMethodTitle
      paymentMethods(
        supportedPaymentMethodCodes: ["online", "autopayment", "sbp"]
      ) {
        code
        title
        description
        isActive
        dates
        change {
          code
          value
          currencyCode
        }
      }
      delivery
      deliveryMethodTitle
      comment
      isAgreementAccepted
      coordinates {
        latitude
        longitude
      }
      address
      porch
      floor
      flat
      datetimeFrom
      datetimeTo
      datetimeCreated
      deliveryPrice
      originalDeliveryPrice
      firstname
      lastname
      phone
      email
      isMy
      orderItems {
        id
        productId
        productCode
        amount
        name
        price
        imageId
        isActive
        quant {
          code
          fullName
          shortName
          multiple
          pricePerUnit
          previousPricePerUnit
          unit
          type
          minAmount
          stepAmount
          amountPerQuant
          currency
          unitCode
        }
        orderItemSum
        isCreateReviewAvailable
        isGift
      }
      orderSum
      originalOrderSum
      invoiceUrl
      change {
        code
        value
        currencyCode
      }
      isAwaitingCancellation
      isCancellable
      trackingNumbers
      minDeliveryTime
      maxDeliveryTime
      isPrivateHouse
      customerOrderNumber
      bankCardID
      isRepeatable
      hasDebt
      isCanPayment
      orderGroup {
        id
        isRepeatable
        hasDebt
        orders {
          id
          number
          statusCode
          isAwaitingCancellation
          paymentDetail {
            isComplete
            paymentPartList {
              vendorFormUrl
              lifetime
            }
          }
          bankCardID
        }
      }
    }
  }
}
"""

# Входные данные для запроса
input_data = {
    "input": {
        "deliveryToken": "eyJ0eXBlIjoiTWFya2V0cGxhY2VcXE1hbmFnZXJcXERlbGl2ZXJ5XFxTbG90XFxEZWxpdmVyeVNsb3RSZWd1bGFyIiwidGl0bGUiOiIxNDowMC0xNTowMCIsImRlbGl2ZXJ5X21ldGhvZCI6InlhcmNoZV9jb3VyaWVyIiwic3RvY2siOjk2LCJpc19kZWZhdWx0IjpmYWxzZSwicGF5bWVudF9tZXRob2RzIjpbIm9ubGluZSIsImNhcmQiXSwidmFyaWFudCI6eyJkYXRlIjoiMjAyMy0wNC0xMyIsImRlbGl2ZXJfYWZ0ZXIiOjAsImRlbGl2ZXJ5X2xpbWl0IjoxMCwiZGVsaXZlcnlfbWV0aG9kX2NvZGUiOiJ5YXJjaGVfY291cmllciIsImVuZCI6IjE1OjAwIiwicHJpY2UiOjAsInN0YXJ0IjoiMTQ6MDAiLCJ0b2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpsZUhBaU9qRTJPREV6Tmpnd01EQXNJbXAwYVNJNkltRTROemhsWWpWaUxXTTBOMlF0TVRGbFl5MDROemxsTFRBMk1qZzVZMkZtTkRFeE15SXNJbVJoZEdVaU9pSXlNREl6TFRBMExURXpJaXdpWm5KdmJTSTZJakUwT2pBd0lpd2lkRzhpT2lJeE5Ub3dNQ0lzSW14aGRDSTZOVFl1TkRVNU1qSTRMQ0pzYjI0aU9qZzBMamswTkRBeE1Td2lZM1puSWpvaVl6Y3daV1F5WVRZdFlUazNOaTAwWWpKaUxUaG1abVl0TnpobE56ZzFaamMxT0dRd0lpd2lkM0pvSWpvaU1HVXlObVF3T0RjdE16VmlNaTB4TVdVMUxUZ3daVEF0TURBMU1EVTJPV0l6WVdZeElpd2laRzBpT2lJMU1qazVPRFpqWWkxak5EWTVMVFJqTVRJdFlXUmxZeTA1T0RReU9HSm1NRFJpTlRjaUxDSmpaeUk2SWpSaU56Tm1abVUyTFdJM05tTXRNVEZsT1MxaU9EWmlMVEF5TkRKak1HRTROREF3WWlJc0ltTjJaMFZKWkNJNkl0Q2lNRFl3SWl3aWJDSTZNVEFzSW1ac0lqb3hNSDAubURkOWZGa09xUWE1OHM3SmJiajFPREYzanJ4bU9zRWJnTDhNQTRFMEZrTSIsIndhcmVob3VzZV9ndWlkIjoiMGUyNmQwODctMzViMi0xMWU1LTgwZTAtMDA1MDU2OWIzYWYxIiwicHJpY2VfdGhyZXNob2xkIjpudWxsfSwiZnJvbSI6IjIwMjMtMDQtMTNUMTQ6MDA6MDArMDc6MDAiLCJ0byI6IjIwMjMtMDQtMTNUMTU6MDA6MDArMDc6MDAifQ==",
        "paymentMethodCode": "online",
        "firstname": "autotest",
        "lastname": "autotest",
        "phone": "+79998887766",
        "email": "vpavlin@test.com",
        "isAgreementAccepted": True,
        "parts": [{"products": [{"id": 4328},{"id": 3253}]}],
        "clientId": "GA1.5.216541125.1636451600"
    }
}

def get_headers(api_token):
    return {
        "Content-Type": "application/json",
        "token": api_token
    }

def rest_query(order_id, order_sum, order_item_id):
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
