from binance.enums import *
from bot.logger import setup_logger

logger = setup_logger()

def place_market_order(client, symbol, side, quantity):
    """
    Market order place karta hai (BUY / SELL)
    """
    try:
        logger.info(f"Placing MARKET order | {side} | {symbol} | Qty: {quantity}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )

        logger.info(f"Market order placed successfully | Order ID: {order.get('orderId')}")
        return order

    except Exception as e:
        logger.error(f"Error while placing market order: {str(e)}")
        return None


def place_limit_order(client, symbol, side, quantity, price):
    """
    Limit order place karta hai (BUY / SELL)
    """
    try:
        logger.info(
            f"Placing LIMIT order | {side} | {symbol} | Qty: {quantity} | Price: {price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC
        )

        logger.info(f"Limit order placed successfully | Order ID: {order.get('orderId')}")
        return order

    except Exception as e:
        logger.error(f"Error while placing limit order: {str(e)}")
        return None

