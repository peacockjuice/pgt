
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
        "deliveryToken": "eyJ0eXBlIjoiTWFya2V0cGxhY2VcXE1hbmFnZXJcXERlbGl2ZXJ5XFxTbG90XFxEZWxpdmVyeVNsb3RSZWd1bGFyIiwidGl0bGUiOiIwOTowMC0xMDowMCIsImRlbGl2ZXJ5X21ldGhvZCI6InlhcmNoZV9jb3VyaWVyIiwic3RvY2siOjk2LCJpc19kZWZhdWx0Ijp0cnVlLCJwYXltZW50X21ldGhvZHMiOlsib25saW5lIiwiY2FyZCJdLCJ2YXJpYW50Ijp7ImRhdGUiOiIyMDIzLTA0LTExIiwiZGVsaXZlcl9hZnRlciI6MCwiZGVsaXZlcnlfbGltaXQiOjEwLCJkZWxpdmVyeV9tZXRob2RfY29kZSI6InlhcmNoZV9jb3VyaWVyIiwiZW5kIjoiMTA6MDAiLCJwcmljZSI6MCwic3RhcnQiOiIwOTowMCIsInRva2VuIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pFMk9ERXhOemN5TURBc0ltcDBhU0k2SW1FNE56aGxZakZsTFdNME4yUXRNVEZsWXkwNE56bGxMVEEyTWpnNVkyRm1OREV4TXlJc0ltUmhkR1VpT2lJeU1ESXpMVEEwTFRFeElpd2labkp2YlNJNklqQTVPakF3SWl3aWRHOGlPaUl4TURvd01DSXNJbXhoZENJNk5UWXVORFU1TWpJNExDSnNiMjRpT2pnMExqazBOREF4TVN3aVkzWm5Jam9pWXpjd1pXUXlZVFl0WVRrM05pMDBZakppTFRobVptWXROemhsTnpnMVpqYzFPR1F3SWl3aWQzSm9Jam9pTUdVeU5tUXdPRGN0TXpWaU1pMHhNV1UxTFRnd1pUQXRNREExTURVMk9XSXpZV1l4SWl3aVpHMGlPaUkxTWprNU9EWmpZaTFqTkRZNUxUUmpNVEl0WVdSbFl5MDVPRFF5T0dKbU1EUmlOVGNpTENKalp5STZJalJpTnpObVptVTJMV0kzTm1NdE1URmxPUzFpT0RaaUxUQXlOREpqTUdFNE5EQXdZaUlzSW1OMlowVkpaQ0k2SXRDaU1EWXdJaXdpYkNJNk1UQXNJbVpzSWpveE1IMC4xMlBwUXM4dE5hZl9YUmE5SUtJVUlpQm5PSl81N2t2c3pVd3VBa2ZyRy1BIiwid2FyZWhvdXNlX2d1aWQiOiIwZTI2ZDA4Ny0zNWIyLTExZTUtODBlMC0wMDUwNTY5YjNhZjEiLCJwcmljZV90aHJlc2hvbGQiOm51bGx9LCJmcm9tIjoiMjAyMy0wNC0xMVQwOTowMDowMCswNzowMCIsInRvIjoiMjAyMy0wNC0xMVQxMDowMDowMCswNzowMCJ9",
        "paymentMethodCode": "online",
        "firstname": "test1",
        "lastname": "test2",
        "phone": "+79234118982",
        "email": "zoshb@bk.ru",
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

