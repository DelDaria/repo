class Tovar():
    # valid categories:
    # food, chemicals, alcohol

    def __init__(self, name, category, unit, price):
        self.name = name
        self.category = category
        self.unit = unit
        self.price = price

    def  is_eatable(self):
        if self.category != 'chemicals':
            return True
        return False

    def price_total(self):
        return self.price*self.unit



class Cart():
    def __init__(self):
        self.list = []

    def add_tovar(self, name, category, unit, price):
        tovar = Tovar(name, category, unit, price)
        self.list.append(tovar)

    def price_total(self):
        sum = 0
        for item in self.list:
            sum += item.price_total()
        return sum

    def is_everything_eatable(self):
        for item in self.list:
            if not item.is_eatable():
                return False
        return True



bread = Tovar('bread', 'food', 2, 10)
beer = Tovar('beer', 'alc', 10, 20)
glass = Tovar('glass', 'chemicals', 1, 300)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
my_cart = Cart()
my_cart.add_tovar('bread', 'food', 2, 10)
my_cart.add_tovar('beer', 'alc', 10, 20)
my_cart.add_tovar('glass', 'chemicals', 1, 300)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

print(my_cart.price_total())
print(my_cart.is_everything_eatable())


