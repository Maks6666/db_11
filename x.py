from sqlalchemy import create_engine, Column, Integer, String, Sequence, CheckConstraint, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

username = 'postgres'
db_password = 134472

db_url = f'postgresql+psycopg2://{username}:{db_password}@localhost:5432/sales_2'
engine = create_engine(db_url)

Base = declarative_base()

class Salesman(Base):
    __tablename__ = "salesman"
    id = Column(Integer, Sequence("id_seq"), primary_key=True)
    name = Column(String(20))
    surname = Column(String(20))

    sales = relationship("Sales", back_populates="salesman")

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, Sequence("id_seq"), primary_key=True)
    cust_name = Column(String(20))
    cust_surname = Column(String(20))

    purchases = relationship("Sales", back_populates="customer")

class Sales(Base):
    __tablename__ = "sales"
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    product = Column(String(20))
    price = Column(Integer, CheckConstraint('price > 0'))

    saler_id = Column(Integer, ForeignKey('salesman.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))

    salesman = relationship("Salesman", back_populates="sales")
    customer = relationship("Customer", back_populates="purchases")

Base.metadata.create_all(bind=engine)

# session creation
Session = sessionmaker(bind=engine)
session = Session()

# Sample data for Salesman table
salesman_data = [
    Salesman(name="John", surname="Doe"),
    Salesman(name="Jane", surname="Smith"),
    Salesman(name="Jim", surname="Beam"),
    Salesman(name="Jack", surname="Daniels"),
    Salesman(name="Jill", surname="Valentine"),
    Salesman(name="Jerry", surname="Seinfeld"),
    Salesman(name="Jessica", surname="Jones"),
    Salesman(name="Joan", surname="Holloway"),
    Salesman(name="Jacob", surname="Black"),
    Salesman(name="Jared", surname="Leto")
]

# Sample data for Customer table
customer_data = [
    Customer(cust_name="Alice", cust_surname="Johnson"),
    Customer(cust_name="Bob", cust_surname="Brown"),
    Customer(cust_name="Charlie", cust_surname="Davis"),
    Customer(cust_name="Diana", cust_surname="Evans"),
    Customer(cust_name="Eve", cust_surname="Wilson"),
    Customer(cust_name="Frank", cust_surname="Garcia"),
    Customer(cust_name="Grace", cust_surname="Miller"),
    Customer(cust_name="Hank", cust_surname="Moore"),
    Customer(cust_name="Ivy", cust_surname="Taylor"),
    Customer(cust_name="Jack", cust_surname="Anderson")
]

# Add the data to the session
session.add_all(salesman_data)
session.add_all(customer_data)
session.commit()

# Get IDs of Salesman and Customer
salesmen = session.query(Salesman).all()
customers = session.query(Customer).all()

# Ensure that salesmen and customers were added
if not salesmen or not customers:
    raise ValueError("Salesmen or customers were not properly added to the database.")

salesmen_ids = [salesman.id for salesman in salesmen]
customer_ids = [customer.id for customer in customers]

# Sample data for Sales table
sales_data = [
    Sales(product="Product1", price=100, saler_id=salesmen_ids[0], customer_id=customer_ids[0]),
    Sales(product="Product2", price=200, saler_id=salesmen_ids[1], customer_id=customer_ids[1]),
    Sales(product="Product3", price=300, saler_id=salesmen_ids[2], customer_id=customer_ids[2]),
    Sales(product="Product4", price=400, saler_id=salesmen_ids[3], customer_id=customer_ids[3]),
    Sales(product="Product5", price=500, saler_id=salesmen_ids[4], customer_id=customer_ids[4]),
    Sales(product="Product6", price=600, saler_id=salesmen_ids[5], customer_id=customer_ids[5]),
    Sales(product="Product7", price=700, saler_id=salesmen_ids[6], customer_id=customer_ids[6]),
    Sales(product="Product8", price=800, saler_id=salesmen_ids[7], customer_id=customer_ids[7]),
    Sales(product="Product9", price=900, saler_id=salesmen_ids[8], customer_id=customer_ids[8]),
    Sales(product="Product10", price=1000, saler_id=salesmen_ids[9], customer_id=customer_ids[9])
]

# Add the sales data to the session
session.add_all(sales_data)
session.commit()
