import requests

class UnrealGameConnector:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def get_game_data(self):
        url = f"{self.api_base_url}/game_data"
        response = requests.get(url)
        return response.json()

    def send_data_to_game(self, data):
        url = f"{self.api_base_url}/update_game"
        response = requests.post(url, json=data)
        return response.json()