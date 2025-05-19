import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder:
    def test_init_with_valid_data(self):
        customer = Customer("Dave")
        coffee = Coffee("Americano")
        order = Order(customer, coffee, 3.5)
        assert order.price == 3.5
        assert order.customer == customer
        assert order.coffee == coffee
    
    def test_price_validation(self):
        customer = Customer("Eve")
        coffee = Coffee("Macchiato")
        with pytest.raises(TypeError):
            Order(customer, coffee, "three")
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.5)
        with pytest.raises(ValueError):
            Order(customer, coffee, 10.5)
    
    def test_price_immutable(self):
        customer = Customer("Frank")
        coffee = Coffee("Flat White")
        order = Order(customer, coffee, 4.0)
        with pytest.raises(AttributeError):
            order.price = 4.5