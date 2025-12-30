import streamlit as st
import os
from dotenv import load_dotenv

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

# Load env variables
load_dotenv()

st.set_page_config(page_title="Trading Bot UI", layout="centered")

st.title("📈 Binance Futures Testnet Trading Bot")
st.caption("Streamlit UI (Optional Bonus)")

# API keys check
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

if not api_key or not api_secret:
    st.error("API keys not found. Please set them in .env file.")
    st.stop()

# Inputs
symbol = st.text_input("Symbol", value="BTCUSDT")
order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT", "STOP_LIMIT"]
)
side = st.selectbox("Side", ["BUY", "SELL"])
quantity = st.text_input("Quantity", value="0.001")

price = None
stop_price = None
limit_price = None

if order_type == "LIMIT":
    price = st.text_input("Limit Price")

if order_type == "STOP_LIMIT":
    stop_price = st.text_input("Stop Price")
    limit_price = st.text_input("Limit Price")

# Place order
if st.button("🚀 Place Order"):
    # Validation
    for check, value in [
        (validate_symbol, symbol),
        (validate_side, side),
        (validate_order_type, order_type),
        (validate_quantity, quantity),
    ]:
        valid, msg = check(value)
        if not valid:
            st.error(msg)
            st.stop()

    bot = BasicBot(api_key, api_secret, testnet=True)

    order = None

    if order_type == "MARKET":
        order = place_market_order(
            bot.client,
            symbol.upper(),
            side,
            float(quantity)
        )

    elif order_type == "LIMIT":
        valid, msg = validate_price(price)
        if not valid:
            st.error(msg)
            st.stop()

        order = place_limit_order(
            bot.client,
            symbol.upper(),
            side,
            float(quantity),
            float(price)
        )

    elif order_type == "STOP_LIMIT":
        for p in [stop_price, limit_price]:
            valid, msg = validate_price(p)
            if not valid:
                st.error(msg)
                st.stop()

        order = place_stop_limit_order(
            bot.client,
            symbol.upper(),
            side,
            float(quantity),
            float(stop_price),
            float(limit_price)
        )

    # Output
    if order:
        st.success("Order request sent successfully")

        st.json({
            "symbol": order.get("symbol"),
            "side": order.get("side"),
            "type": order.get("type"),
            "quantity": order.get("origQty"),
            "status": order.get("status"),
            "orderId": order.get("orderId"),
        })
    else:
        st.error("Order request failed. Check logs for details.")

