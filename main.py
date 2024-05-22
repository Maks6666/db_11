from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date, CheckConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text

username = 'postgres'
db_password = 134472

db_url = f'postgresql+psycopg2://{username}:{db_password}@localhost:5432/sales'
engine = create_engine(db_url)


Base = declarative_base()

class Sales(Base):
    __tablename__ = "sales"
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    product = Column(String(20), nullable=False)
    price = Column(Integer, CheckConstraint('price > 0'), nullable=False)


class Salesman(Base):
    __tablename__ = "salesman"
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    name = Column(String(20), nullable=False)
    surname = Column(String(20), nullable=False)



class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    cust_name = Column(String(20), nullable=False)
    cust_surname = Column(String(20), nullable=False)


Base.metadata.create_all(bind=engine)

# session creation
Session = sessionmaker(bind=engine)
session = Session()

# add data

sales_data = [
    Sales(product="Product1", price=100),
    Sales(product="Product2", price=200),
    Sales(product="Product3", price=300),
    Sales(product="Product4", price=400),
    Sales(product="Product5", price=500),
    Sales(product="Product6", price=600),
    Sales(product="Product7", price=700),
    Sales(product="Product8", price=800),
    Sales(product="Product9", price=900),
    Sales(product="Product10", price=1000)
]

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
# session.add_all(sales_data)
# session.add_all(salesman_data)
# session.add_all(customer_data)


session.commit()



while True:

    tables = ["sales", "salesman", "customer"]

    print("Avaliable commands: ")
    print("1 - to insert value")
    print("2 - to update value")
    print("3 - to delete value")
    print("0 - to exit")

    command = int(input("Input your command: "))

    if command == 0:
        break
    elif command == 1:
        table = input("Input your table name:").lower()

        if table in tables:
            iter = int(input("How many rows do you want to add?: "))
            for i in range(iter):
                if table == "sales":
                    sale = Sales(product=input("Input product name: "),
                                 price=int(input("Input price: ")))
                    session.add(sale)
                elif table == "salesman":
                    salesman = Salesman(name=input("Input name: "),
                                        surname=input("Input surname: "))
                    session.add(salesman)
                elif table == "customer":
                    customer = Customer(cust_name=input("Input name: "),
                                        cust_surname=input("Input surname: "))
                    session.add(customer)
            session.commit()
        else:
            print("Invalid table name.")

    elif command == 2:
        table = input("Input your table name:").lower()

        if table == "sales":
            product_name = input("Input name of product: ")



            sale = session.query(Sales).filter(
                Sales.product == product_name
            ).first()

            sale.product = input("Input new name of product: ")
            sale.price = int(input("Input new price: "))
            session.commit()

        elif table == "salesman":
            name = input("Input name of product: ")

            salesman = session.query(Salesman).filter(
                Salesman.name == name
            ).first()

            salesman.name = input("Input new name of product: ")
            salesman.surname = int(input("Input new price: "))
            session.commit()


        elif table == "customer":
            cust_name = input("Input name of product: ")

            customer = session.query(Customer).filter(
                Customer.cust_name == cust_name
            ).first()

            customer.cust_name = input("Input new name of product: ")
            customer.cust_price = int(input("Input new price: "))
            session.commit()

# session.close()


    elif command == 3:
        table = input("Input your table name:").lower()

        if table == "sales":
            product_name = input("Input name of product: ")

            sale = session.query(Sales).filter(
                Sales.product == product_name
            ).first()

            session.delete(sale)
            session.commit()

        elif table == "salesman":
            name = input("Input name of product: ")

            salesman = session.query(Salesman).filter(
                Salesman.name == name
            ).first()

            session.delete(salesman)
            session.commit()


        elif table == "customer":
            cust_name = input("Input name of product: ")

            customer = session.query(Customer).filter(
                Customer.cust_name == cust_name
            ).first()

            session.delete(customer)
            session.commit()




