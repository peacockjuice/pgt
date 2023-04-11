
# Запрос GraphQL
query = """
mutation ($input: CreateOrderInput!) {
  createOrder(input: $input) {
    id
    orders {
      id
      statusCode
      paymentDetail {
        isComplete
        paymentPartList {
          vendorFormUrl
          lifetime
        }
      }
    }
  }
}
"""

# Входные данные для запроса
input_data = {
    "input": {
        "deliveryToken": "eyJ0eXBlIjoiTWFya2V0cGxhY2VcXE1hbmFnZXJcXERlbGl2ZXJ5XFxTbG90XFxEZWxpdmVyeVNsb3RSZWd1bGFyIiwidGl0bGUiOiIxOTowMC0yMDowMCIsImRlbGl2ZXJ5X21ldGhvZCI6InlhcmNoZV9jb3VyaWVyIiwic3RvY2siOjk2LCJpc19kZWZhdWx0IjpmYWxzZSwicGF5bWVudF9tZXRob2RzIjpbIm9ubGluZSIsImNhcmQiXSwidmFyaWFudCI6eyJkYXRlIjoiMjAyMy0wNC0xMSIsImRlbGl2ZXJfYWZ0ZXIiOjAsImRlbGl2ZXJ5X2xpbWl0IjoxMCwiZGVsaXZlcnlfbWV0aG9kX2NvZGUiOiJ5YXJjaGVfY291cmllciIsImVuZCI6IjIwOjAwIiwicHJpY2UiOjAsInN0YXJ0IjoiMTk6MDAiLCJ0b2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpsZUhBaU9qRTJPREV5TVRNeU1EQXNJbXAwYVNJNkltRTROemhsWWpNMUxXTTBOMlF0TVRGbFl5MDROemxsTFRBMk1qZzVZMkZtTkRFeE15SXNJbVJoZEdVaU9pSXlNREl6TFRBMExURXhJaXdpWm5KdmJTSTZJakU1T2pBd0lpd2lkRzhpT2lJeU1Eb3dNQ0lzSW14aGRDSTZOVFl1TkRVNU1qSTRMQ0pzYjI0aU9qZzBMamswTkRBeE1Td2lZM1puSWpvaVl6Y3daV1F5WVRZdFlUazNOaTAwWWpKaUxUaG1abVl0TnpobE56ZzFaamMxT0dRd0lpd2lkM0pvSWpvaU1HVXlObVF3T0RjdE16VmlNaTB4TVdVMUxUZ3daVEF0TURBMU1EVTJPV0l6WVdZeElpd2laRzBpT2lJMU1qazVPRFpqWWkxak5EWTVMVFJqTVRJdFlXUmxZeTA1T0RReU9HSm1NRFJpTlRjaUxDSmpaeUk2SWpSaU56Tm1abVUyTFdJM05tTXRNVEZsT1MxaU9EWmlMVEF5TkRKak1HRTROREF3WWlJc0ltTjJaMFZKWkNJNkl0Q2lNRFl3SWl3aWJDSTZNVEFzSW1ac0lqb3hNSDAuMmpfWTJyTk50TEs1RnlOdnBfaUFoUTIwZFpZVUkxSDhCVFliOTVhdzR2QSIsIndhcmVob3VzZV9ndWlkIjoiMGUyNmQwODctMzViMi0xMWU1LTgwZTAtMDA1MDU2OWIzYWYxIiwicHJpY2VfdGhyZXNob2xkIjpudWxsfSwiZnJvbSI6IjIwMjMtMDQtMTFUMTk6MDA6MDArMDc6MDAiLCJ0byI6IjIwMjMtMDQtMTFUMjA6MDA6MDArMDc6MDAifQ==",
        "paymentMethodCode": "online",
        "firstname": "autotest",
        "lastname": "autotest",
        "phone": "+79998887766",
        "email": "vpavlin@test.com",
        "isAgreementAccepted": True,
        "parts": [{"products": [{"id": 4328}]}],
        "clientId": "GA1.5.216541125.1636451600",
    }
}

def get_headers(api_token):
    return {
        "Content-Type": "application/json",
        "token": api_token
    }

