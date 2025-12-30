from binance import Client
from config.settings import BINANCE_TESTNET_URL
from bot.logger import setup_logger

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        # Logger setup
        self.logger = setup_logger()

        # Binance client initialize
        self.client = Client(api_key, api_secret)

        if testnet:
            # Futures testnet URL set kar rahe hain
            self.client.FUTURES_URL = BINANCE_TESTNET_URL
            self.logger.info("Connected to Binance Futures Testnet")

