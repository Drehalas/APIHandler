from unreal_game.unreal_connector import UnrealGameConnector
from gameshift.gameshift_connector import GameShiftConnector
from solanapay.solanapay_connector import SolanaPayConnector

class GameHandler:
    def __init__(self, unreal_api_base_url, gameshift_api_base_url, gameshift_api_key, solanapay_api_base_url):
        self.unreal_game = UnrealGameConnector(unreal_api_base_url)
        self.gameshift = GameShiftConnector(gameshift_api_base_url, gameshift_api_key)
        self.solanapay = SolanaPayConnector(solanapay_api_base_url)

    def get_combined_game_data(self, user_id):
        game_data = self.unreal_game.get_game_data()
        user_data = self.gameshift.fetch_user(user_id)
        user_assets = self.gameshift.fetch_user_assets(user_id)
        combined_data = {**game_data, **user_data, 'assets': user_assets}
        return combined_data

    def update_game_and_player_stats(self, game_data, player_stats):
        self.unreal_game.send_data_to_game(game_data)
        self.gameshift.update_player_stats(player_stats)

    def handle_payment(self, amount, player_id):
        payment_response = self.solanapay.create_transfer(amount, "sender_wallet_address", player_id)
        return payment_response

    def transfer_game_currency(self, amount, sender_id, receiver_id):
        transfer_response = self.gameshift.transfer_currency(amount, sender_id, receiver_id)
        return transfer_response

    def create_payment_qr(self, amount, recipient):
        qr_response = self.solanapay.create_qr(amount, recipient)
        return qr_response


# Example usage
if __name__ == "__main__":
    handler = GameHandler('https://api.unrealengine.com', 'https://api.gameshift.dev', 'your_gameshift_api_key', 'https://api.solanapay.com')
    combined_data = handler.get_combined_game_data('user123')
    print(f"Combined Data: {combined_data}")

    game_data = {"new_game_data": "Updated Game Data"}
    player_stats = {"new_player_stats": "Updated Player Stats"}
    handler.update_game_and_player_stats(game_data, player_stats)

    payment_response = handler.handle_payment(100, "player123_wallet_address")
    print(f"Payment Response: {payment_response}")

    transfer_response = handler.transfer_game_currency(50, "user123", "user456")
    print(f"Transfer Response: {transfer_response}")

    qr_response = handler.create_payment_qr(50, "recipient_wallet_address")
    print(f"QR Response: {qr_response}")