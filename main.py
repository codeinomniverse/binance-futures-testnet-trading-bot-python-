from dotenv import load_dotenv
import os

from bot.basic_bot import BasicBot
from bot.orders import place_market_order, place_limit_order
from bot.validator import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from config.settings import ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT

def main():
    load_dotenv()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        print("❌ API keys not found. Please check .env file")
        return

    # User inputs (CLI)
    symbol = input("Enter Symbol (e.g. BTCUSDT): ").upper()
    order_type = input("Enter Order Type (MARKET / LIMIT): ").upper()
    side = input("Enter Side (BUY / SELL): ").upper()
    quantity = input("Enter Quantity: ")

    # Validations
    valid, msg = validate_symbol(symbol)
    if not valid:
        print(f"❌ {msg}")
        return

    valid, msg = validate_order_type(order_type)
    if not valid:
        print(f"❌ {msg}")
        return

    valid, msg = validate_side(side)
    if not valid:
        print(f"❌ {msg}")
        return

    valid, msg = validate_quantity(quantity)
    if not valid:
        print(f"❌ {msg}")
        return

    # Bot initialize
    bot = BasicBot(api_key, api_secret, testnet=True)

    # Order execution
    if order_type == ORDER_TYPE_MARKET:
        order = place_market_order(
            bot.client,
            symbol,
            side,
            float(quantity)
        )

    elif order_type == ORDER_TYPE_LIMIT:
        price = input("Enter Limit Price: ")

        valid, msg = validate_price(price)
        if not valid:
            print(f"❌ {msg}")
            return

        order = place_limit_order(
            bot.client,
            symbol,
            side,
            float(quantity),
            float(price)
        )

    else:
        print("❌ Unsupported order type")
        return

    # Output
    if order:
        print("\n================= ORDER STATUS =================")
        print("✅ Order Placed Successfully")
        print(f"Symbol       : {order.get('symbol')}")
        print(f"Side         : {order.get('side')}")
        print(f"Order Type   : {order.get('type')}")
        print(f"Quantity     : {order.get('origQty')}")
        print(f"Status       : {order.get('status')}")
        print(f"Order ID     : {order.get('orderId')}")
        print("===============================================\n")
    else:
        print("❌ Order failed. Check logs for details.")

if __name__ == "__main__":
    main()

