import requests

class GameShiftConnector:
    def __init__(self, api_base_url, api_key):
        self.api_base_url = api_base_url
        self.headers = {'Authorization': f'Bearer {api_key}'}

    def fetch_user(self, user_id):
        url = f"{self.api_base_url}/users/{user_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def fetch_user_assets(self, user_id):
        url = f"{self.api_base_url}/users/{user_id}/assets"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def transfer_currency(self, amount, sender_id, receiver_id):
        url = f"{self.api_base_url}/users/{sender_id}/transfer-currency"
        data = {'amount': amount, 'receiver_id': receiver_id}
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()