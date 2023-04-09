
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
        "deliveryToken": "eyJ0eXBlIjoiTWFya2V0cGxhY2VcXE1hbmFnZXJcXERlbGl2ZXJ5XFxTbG90XFxEZWxpdmVyeVNsb3RSZWd1bGFyIiwidGl0bGUiOiIxMTowMC0xMjowMCIsImRlbGl2ZXJ5X21ldGhvZCI6InlhcmNoZV9jb3VyaWVyIiwic3RvY2siOjM5MiwiaXNfZGVmYXVsdCI6ZmFsc2UsInBheW1lbnRfbWV0aG9kcyI6WyJvbmxpbmUiLCJjYXJkIl0sInZhcmlhbnQiOnsiZGF0ZSI6IjIwMjMtMDQtMTEiLCJkZWxpdmVyX2FmdGVyIjowLCJkZWxpdmVyeV9saW1pdCI6MTAsImRlbGl2ZXJ5X21ldGhvZF9jb2RlIjoieWFyY2hlX2NvdXJpZXIiLCJlbmQiOiIxMjowMCIsInByaWNlIjowLCJzdGFydCI6IjExOjAwIiwidG9rZW4iOiJleUpoYkdjaU9pSklVekkxTmlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKbGVIQWlPakUyT0RFeE9EUTBNREFzSW1wMGFTSTZJbVptTlRBMFltRXlMV00wWW1ZdE1URmxZeTFoT1dRMkxUQXlNRFV5TTJZMU5tVTFOU0lzSW1SaGRHVWlPaUl5TURJekxUQTBMVEV4SWl3aVpuSnZiU0k2SWpFeE9qQXdJaXdpZEc4aU9pSXhNam93TUNJc0lteGhkQ0k2TlRZdU5UQXpOekF5TENKc2IyNGlPamcxTGpBM056UXhPU3dpWTNabklqb2lPR1JqWVRnMFkySXRZakF3TlMwME1UTTRMV0k0T0RJdE56YzBORE5tTURJMllqUmhJaXdpZDNKb0lqb2laR1EyTlRoaU16RXRObUkyWWkweE1XVTJMVGd3WmpFdE1EQTFNRFUyWVRrMVlqZ3lJaXdpWkcwaU9pSTFNams1T0RaallpMWpORFk1TFRSak1USXRZV1JsWXkwNU9EUXlPR0ptTURSaU5UY2lMQ0pqWnlJNklqUmlOek5tWm1VMkxXSTNObU10TVRGbE9TMWlPRFppTFRBeU5ESmpNR0U0TkRBd1lpSXNJbU4yWjBWSlpDSTZJbFF3TnpZaUxDSnNJam94TUN3aVptd2lPakV3ZlEucGJxdGh3VG5fT3lhN19tR3ZkTUNtRzMtVkt4ZlpsZm8tRkpjb1Q1TjhJRSIsIndhcmVob3VzZV9ndWlkIjoiZGQ2NThiMzEtNmI2Yi0xMWU2LTgwZjEtMDA1MDU2YTk1YjgyIiwicHJpY2VfdGhyZXNob2xkIjpudWxsfSwiZnJvbSI6IjIwMjMtMDQtMTFUMTE6MDA6MDArMDc6MDAiLCJ0byI6IjIwMjMtMDQtMTFUMTI6MDA6MDArMDc6MDAifQ==",
        "paymentMethodCode": "online",
        "firstname": "test1",
        "lastname": "test2",
        "phone": "+79234118982",
        "email": "zoshb@bk.ru",
        "isAgreementAccepted": True,
        "parts": [{"products": [{"id": 4328}]}],
        "clientId": "GA1.6.974243547.1635827537",
    }
}

def get_headers(api_token):
    return {
        "Content-Type": "application/json",
        "token": api_token
    }

