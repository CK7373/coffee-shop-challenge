import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_init_with_valid_name(self):
        customer = Customer("Alice")
        assert customer.name == "Alice"
    
    def test_init_with_invalid_name_type(self):
        with pytest.raises(TypeError):
            Customer(123)
    
    def test_init_with_long_name(self):
        with pytest.raises(ValueError):
            Customer("ThisNameIsWayTooLong")
    
    def test_name_setter(self):
        customer = Customer("Bob")
        customer.name = "Robert"
        assert customer.name == "Robert"
    
    def test_create_order(self):
        customer = Customer("Charlie")
        coffee = Coffee("TestCoffee")
        order = customer.create_order(coffee, 5.0)
        assert order in Order.all
        assert order.customer == customer
        assert order.coffee == coffee