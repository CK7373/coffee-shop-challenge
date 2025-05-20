COFFEE SHOP CHALLENGE

Coffee Shop Challenge Overview This Python project models a coffee shop domain with three main entities: Coffee, Customer, and Order. It demonstrates object-oriented programming principles and relationship management in Python.

Domain Model Coffee (1) ← (n) Order (n) → (1) Customer A Coffee has many Orders A Customer has many Orders An Order belongs to one Customer and one Coffee Coffee and Customer have a many-to-many relationship through Order

Project Structure coffee-shop-challenge/ ├── Pipfile ├── debug.py ├── customer.py # Customer class implementation ├── coffee.py # Coffee class implementation ├── order.py # Order class implementation └── tests/ ├── customer_test.py ├── coffee_test.py └── order_test.py Installation Clone the repository:

bash git clone git@github.com:/coffee-shop-challenge.git cd coffee-shop-challenge Set up the environment:

bash pipenv install pipenv shell

Class Specifications Customer init(self, name)

Stores a name (must be string, 1-15 characters)

Properties: name (getter/setter with validation)

Methods: orders() - Returns all orders for this customer coffees() - Returns unique list of coffees ordered create_order(coffee, price) - Creates new order

Coffee init(self, name) Stores a name (must be string, ≥3 characters)

Properties: name (getter only, immutable)

Methods: orders() - Returns all orders for this coffee customers() - Returns unique list of customers who ordered it num_orders() - Returns total order count average_price() - Returns mean order price

Order init(self, customer, coffee, price) Requires Customer instance, Coffee instance, and price (float, 1.0-10.0)

Properties: customer (getter with type checking) coffee (getter with type checking) price (getter only, immutable with validation)

Testing Run tests from the project root:

bash python -m pytest tests/ Example Usage python from customer import Customer from coffee import Coffee from order import Order

Create instances
customer = Customer(“Alice”) coffee = Coffee(“Latte”)

Create order
order = customer.create_order(coffee, 5.99)

Get aggregates
print(f”Total orders for {coffee.name}: {coffee.num_orders()}”) print(f”Average price: ${coffee.average_price():.2f}”) Requirements Python 3.8+

pipenv (for virtual environment)

License MIT License

Contacts claire.kariuki@student.moringaschool.com
