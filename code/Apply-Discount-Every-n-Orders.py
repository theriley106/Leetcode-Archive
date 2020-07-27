class Cashier(object, ):

    def __init__(self, n, discount, products, prices):
        self.count = 0
        self.price_lookup = {}
        for (i, val) in enumerate(products):
            self.price_lookup[val] = prices[i]
        self.discount = discount
        self.n = n

    def getBill(self, product, amount):
        self.count += 1
        isDiscount = ((self.count % self.n) == 0)
        cost = 0
        for (i, val) in enumerate(product):
            cost += (self.price_lookup[val] * amount[i])
        if isDiscount:
            cost = (float(cost) - ((self.discount * float(cost)) / 100))
        return float(cost)