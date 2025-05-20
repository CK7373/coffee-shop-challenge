from coffee import Coffee
from order import Order
from customer import Customer
import pytest


class TestCoffee:
    def test_init_with_valid_name(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"
    
    def test_init_with_invalid_name_type(self):
        with pytest.raises(TypeError):
            Coffee(123)
    
    def test_init_with_short_name(self):
        with pytest.raises(ValueError):
            Coffee("La")
    
    def test_name_immutable(self):
        coffee = Coffee("Mocha")
        with pytest.raises(AttributeError):
            coffee.name = "New Mocha"
    
    def test_num_orders(self):
        coffee = Coffee("TestCoffee")
        assert coffee.num_orders() == 0