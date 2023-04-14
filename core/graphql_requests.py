import requests


def get_headers(api_token):
    return {
        "Content-Type": "application/json",
        "token": api_token
    }


def send_graphql_request(bmp_api_url, bmp_api_token, query, input_data):
    bmp_api_url_graphql = f"{bmp_api_url}/graphql"
    headers = get_headers(bmp_api_token)
    response = requests.post(bmp_api_url_graphql, headers=headers, json={"query": query, "variables": input_data})
    response_data = response.json()
    assert response.status_code == 200
    assert "errors" not in response_data
    return response_data