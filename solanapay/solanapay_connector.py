import requests

class SolanaPayConnector:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def create_qr(self, amount, recipient):
        url = f"{self.api_base_url}/createQR"
        data = {"amount": amount, "recipient": recipient}
        response = requests.post(url, json=data)
        return response.json()

    def create_transfer(self, amount, sender, recipient):
        url = f"{self.api_base_url}/createTransfer"
        data = {"amount": amount, "sender": sender, "recipient": recipient}
        response = requests.post(url, json=data)
        return response.json()

    def fetch_transaction(self, transaction_id):
        url = f"{self.api_base_url}/fetchTransaction/{transaction_id}"
        response = requests.get(url)
        return response.json()
