from binance.enums import *
from bot.logger import setup_logger

logger = setup_logger()


def place_market_order(client, symbol, side, quantity):
    """
    Market order (BUY / SELL)
    """
    try:
        logger.info(
            f"Placing MARKET order | {side} | {symbol} | Qty: {quantity}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )

        logger.info(f"Market order placed | Order ID: {order.get('orderId')}")
        return order

    except Exception as e:
        logger.error(f"Market order error: {str(e)}")
        return None


def place_limit_order(client, symbol, side, quantity, price):
    """
    Limit order (BUY / SELL)
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

        logger.info(f"Limit order placed | Order ID: {order.get('orderId')}")
        return order

    except Exception as e:
        logger.error(f"Limit order error: {str(e)}")
        return None


def place_stop_limit_order(client, symbol, side, quantity, stop_price, limit_price):
    """
    Stop-Limit order (BONUS)
    """
    try:
        logger.info(
            f"Placing STOP-LIMIT order | {side} | {symbol} | "
            f"Qty: {quantity} | Stop: {stop_price} | Limit: {limit_price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=quantity,
            stopPrice=stop_price,
            price=limit_price,
            timeInForce=TIME_IN_FORCE_GTC
        )

        logger.info(f"Stop-Limit order placed | Order ID: {order.get('orderId')}")
        return order

    except Exception as e:
        logger.error(f"Stop-Limit order error: {str(e)}")
        return None

