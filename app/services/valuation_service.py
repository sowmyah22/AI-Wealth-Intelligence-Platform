def calculate_holding_value(
    quantity: int,
    current_price: float
):

    return quantity * current_price


def calculate_invested_value(
    quantity: int,
    buy_price: float
):

    return quantity * buy_price


def calculate_profit_loss(
    invested_value: float,
    current_value: float
):

    return current_value - invested_value