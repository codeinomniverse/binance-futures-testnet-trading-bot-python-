from dotenv import load_dotenv
import os

from bot.basic_bot import BasicBot
from bot.orders import (
    place_market_order,
    place_limit_order,
    place_stop_limit_order
)
from bot.validator import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from config.settings import (
    ORDER_TYPE_MARKET,
    ORDER_TYPE_LIMIT,
    ORDER_TYPE_STOP_LIMIT
)

def main():
    load_dotenv()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        print("❌ API keys not found. Please check .env file")
        return

    # ---------------- CLI INPUT ----------------
    symbol = input("Enter Symbol (e.g. BTCUSDT): ").upper()
    order_type = input(
        "Enter Order Type (MARKET / LIMIT / STOP_LIMIT): "
    ).upper()
    side = input("Enter Side (BUY / SELL): ").upper()
    quantity = input("Enter Quantity: ")

    # ---------------- VALIDATION ----------------
    for check, value in [
        (validate_symbol, symbol),
        (validate_order_type, order_type),
        (validate_side, side),
        (validate_quantity, quantity),
    ]:
        valid, msg = check(value)
        if not valid:
            print(f"❌ {msg}")
            return

    # ---------------- BOT INIT ----------------
    bot = BasicBot(api_key, api_secret, testnet=True)

    # ---------------- ORDER EXECUTION ----------------
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

    elif order_type == ORDER_TYPE_STOP_LIMIT:
        stop_price = input("Enter Stop Price: ")
        limit_price = input("Enter Limit Price: ")

        for p in [stop_price, limit_price]:
            valid, msg = validate_price(p)
            if not valid:
                print(f"❌ {msg}")
                return

        order = place_stop_limit_order(
            bot.client,
            symbol,
            side,
            float(quantity),
            float(stop_price),
            float(limit_price)
        )

    else:
        print("❌ Unsupported order type")
        return

    # ---------------- OUTPUT ----------------
    if order:
        status = order.get("status")

        print("\n================= ORDER STATUS =================")
        print("✅ Order Request Successful")
        print(f"Symbol       : {order.get('symbol')}")
        print(f"Side         : {order.get('side')}")
        print(f"Order Type   : {order.get('type')}")
        print(f"Quantity     : {order.get('origQty')}")
        print(f"Status       : {status}")
        print(f"Order ID     : {order.get('orderId')}")

        if status != "FILLED":
            print("ℹ️ Note: Order is placed but not filled yet.")

        print("===============================================\n")
    else:
        print("❌ Order request failed. Check logs for details.")

if __name__ == "__main__":
    main()

