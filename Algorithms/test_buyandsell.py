from buyandsell import *

order = TheoryOfCrypto()


def test_buy_book():
    order.buy_book(100)
    assert order.buyOffers == [100]
    order.buy_book(108)
    assert order.buyOffers == [100, 108]
    order.sellOffers(109)
    assert order.sellOffers == [109]
