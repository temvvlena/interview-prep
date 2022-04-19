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


OfferstoBUY: [$100, $100, $99, 120, $97, $90, 120]

OfferstoSELL:[$109, $110, $110, $114, $115$, 119, 80]   =>



BUY [100,108]
SELL [109]
Input = 109
"""

from heapq import heappush, heappop, heapify


class TheoryOfCrypto:
    def __init__(self):
        self.buyOffers = []
        self.sellOffers = []

    def buy_book(self, buyPrice):
        if not self.sellOffers:
            self.buyOffers.append(-buyPrice)
        else:
            heapify(self.sellOffers)
            minimumSellOffer = self.sellOffers[0]
            if buyPrice > minimumSellOffer:
                print(f'\n Match occurred {buyPrice} wants to buy {minimumSellOffer} \n')
                heappop(self.sellOffers)
            else:
                heappush(self.buyOffers, -buyPrice)

    def sell_book(self, sellPrice):
        if not self.buyOffers:
            self.sellOffers.append(sellPrice)
        else:
            heapify(self.buyOffers)
            maximumBuyOffer = -self.buyOffers[0]
            if maximumBuyOffer > sellPrice:
                print(f'\n Match occured {maximumBuyOffer} wants to buy {sellPrice} \n')
                heappop(self.buyOffers)
            else:
                heappush(self.sellOffers, sellPrice)


order = TheoryOfCrypto()
order.buy_book(100)
order.buy_book(109)
order.sell_book(111)
order.sell_book(90)
order.buy_book(200)
