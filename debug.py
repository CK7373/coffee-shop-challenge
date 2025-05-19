from customer import Customer
from coffee import Coffee
from order import Order

def debug_console():
    # Create some coffees
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    
    # Create some customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    
    # Create orders
    order1 = Order(alice, espresso, 2.5)
    order2 = Order(alice, latte, 3.0)
    order3 = Order(bob, cappuccino, 3.5)
    order4 = Order(bob, espresso, 2.5)
    
    # Test relationships
    print(f"{alice.name}'s orders: {[o.coffee.name for o in alice.orders()]}")
    print(f"{bob.name}'s coffees: {[c.name for c in bob.coffees()]}")
    print(f"Espresso orders: {espresso.num_orders()}")
    print(f"Latte average price: {latte.average_price()}")
    
    # Test creating order through customer
    new_order = alice.create_order(cappuccino, 4.0)
    print(f"Alice's new order: {new_order.coffee.name} at ${new_order.price}")

if __name__ == "__main__":
    debug_console()