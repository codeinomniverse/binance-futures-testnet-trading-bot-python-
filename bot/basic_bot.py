from binance import Client
from config.settings import BINANCE_TESTNET_URL
from bot.logger import setup_logger

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        # Logger setup
        self.logger = setup_logger()

        # Binance client init
        self.client = Client(api_key, api_secret)

        if testnet:
            # Futures Testnet URL
            self.client.FUTURES_URL = BINANCE_TESTNET_URL
            self.logger.info("Connected to Binance Futures Testnet")

        # Futures leverage set (IMPORTANT)
        try:
            self.client.futures_change_leverage(
                symbol="BTCUSDT",
                leverage=1
            )
            self.logger.info("Leverage set to 1x for BTCUSDT")
        except Exception as e:
            self.logger.error(f"Error setting leverage: {str(e)}")

