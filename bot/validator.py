from config.settings import (
    ORDER_TYPE_MARKET,
    ORDER_TYPE_LIMIT,
    SIDE_BUY,
    SIDE_SELL
)

def validate_symbol(symbol):
    if not symbol or not isinstance(symbol, str):
        return False, "Invalid trading symbol"
    return True, ""


def validate_side(side):
    if side not in [SIDE_BUY, SIDE_SELL]:
        return False, "Order side must be BUY or SELL"
    return True, ""


def validate_order_type(order_type):
    if order_type not in [ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT]:
        return False, "Order type must be MARKET or LIMIT"
    return True, ""


def validate_quantity(quantity):
    try:
        qty = float(quantity)
        if qty <= 0:
            return False, "Quantity must be greater than zero"
        return True, ""
    except ValueError:
        return False, "Quantity must be a number"


def validate_price(price):
    try:
        pr = float(price)
        if pr <= 0:
            return False, "Price must be greater than zero"
        return True, ""
    except ValueError:
        return False, "Price must be a number"

