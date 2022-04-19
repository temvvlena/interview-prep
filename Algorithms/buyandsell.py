"""
You operate a marketplace for buying & selling used textbooks For a given textbook eg“TheoryofCryptography”
there are people who want to buy this textbook and people who want to sell

OfferstoBUY: --> [ $90, 90, 90, 90, $100, $99, $97, $90, 120 ]

OfferstoSELL: -->   $80, $110, $110, $114, $115$, 119
"""

"""
buy ->  [100,]

sell -> []

input = 109


OfferstoBUY: [$100, $100, $99, $99, $97, $90, 120]

OfferstoSELL:[$109, $110, $110, $114, $115$, 119, 80]   =>



BUY [100,108]
SELL [109]
Input = 109
"""

from heapq import heappush, heappop, heapify
class TheoryOfCrypto:
    def __init__(self):
        self.buyOffers = heapify([])
        self.sellOffers = []

    def buy_book(self, buyPrice):
        if not self.sellOffers:
            self.buyOffers.append(-buyPrice)

    def sell_book(self, sellPrice):
        if not self.buyOffers:
            self.sellOffers.append(sellPrice)
        self.buyOffers = heapify(self.buyOffers)
        self.buyOffers.heapq.heappush(sellPrice)
        maxPriceFromBuyOffer = self.buyOffers[-1]
        if maxPriceFromBuyOffer < sellPrice:
            self.sellOffers.append(sellPrice)
        else:
            buy_match = self.buyOffers.heapq.heappop()
            print(f'Matched+{buy_match} and {sellPrice}')


order = TheoryOfCrypto()
order.buy_book(100)
order.sell_book(109)
order.buy_book(111)


