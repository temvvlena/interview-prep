orderHistory = [
    {
        "date": 1,
        "type": "buy",
        "price": 25,
        "amount": 5
    },
    {
        "date": 2,
        "type": "buy",
        "price": 40,
        "amount": 10
    },
    {
        "date": 3,
        "type": "sell",
        "price": 42,
        "amount": 7
    },
    {
        "date": 4,
        "type": "sell",
        "price": 3,
        "amount": 1
    },
    {
        "date": 5,
        "type": "buy",
        "price": 25,
        "amount": 5
    },
    {
        "date": 6,
        "type": "sell",
        "price": 20,
        "amount": 10
    }
]

"""
Customers can buy and sell BTC on our platform. We want to help them know what taxable gains and/or losses they have 
to help them file taxes. When BTC is purchased, we note the time and value in dollars known as the cost basis. 
When BTC is sold, at least one of these earlier purchases are fully or partially consumed. The resulting difference 
in the dollar value when sold (the proceeds) and the cost basis is the gain (or a loss if negative).

We'd like to get an output of the gain/loss data that includes the date of sale, date of acquisition, cost basis, 
proceeds, gains, and amount of BTC. We'd also like to be able to see the current positions (date, amount and cost basis)
left at any time (just internal, to print to screen or something simple).
"""


def calculate_gains_or_losses(history):
    total = 0
    if not history:
        return 'Please put at least one order'
    for order in history:
        if order["type"] == 'buy':
            total += (order["amount"] * order["price"])
        else:
            total -= (order["amount"] * order["price"])
    return f"Gained:{total}" if total > 0 else f"Lost:{total}"


def test_calculate_gains_or_losses():
    assert calculate_gains_or_losses(orderHistory) == "Gained:153"
    assert calculate_gains_or_losses({}) == 'Please put at least one order'
