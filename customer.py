from coffee import Coffee
from order import Order

class Customer:
    all = []
    
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name
    
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be of type Coffee")
        return Order(self, coffee, price)
