from buyandsell import *

order = TheoryOfCrypto()


def test_buy_book():
    order.buy_book(100)
    assert len(order.buyOffers) == 1
    order.buy_book(109)
    assert len(order.buyOffers) == 2
    order.sell_book(111)
    assert len(order.sellOffers) == 1
    # Match occurred
    order.sell_book(90)
    assert len(order.buyOffers) == 1
    print(order.buyOffers, order.sellOffers)
    # Match occurred
    order.buy_book(200)
    assert len(order.sellOffers) == 0
    print(order.buyOffers, order.sellOffers)


def test_many_orders():
    buyList = [100, 100, 120, 99, 135, 90, 200]
    sellList = [109, 110, 110, 114, 115, 119, 80]
    for index in range(len(buyList)):
        order.buy_book(buyList[index])
        order.sell_book(sellList[index])
    assert len(order.buyOffers) == 3
    assert len(order.sellOffers) == 3
    assert order.buyOffers == [-100, -90, -99]
    assert order.sellOffers == [114, 119, 115]





