from sqlalchemy import create_engine, Column, Integer, func, String, Sequence, Date, CheckConstraint, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import or_, and_
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text

username = 'postgres'
db_password = "password"

db_url = f'postgresql+psycopg2://{username}:{db_password}@localhost:5432/sales_2'
engine = create_engine(db_url)


Base = declarative_base()

class Salesman(Base):
    __tablename__ = 'salesmen'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)

    sales = relationship('Sales', back_populates='salesman')

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cust_name = Column(String)
    cust_surname = Column(String)

    sales = relationship('Sales', back_populates='customer')

class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product = Column(String)
    price = Column(Integer)
    salesman_id = Column(Integer, ForeignKey('salesmen.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    salesman = relationship('Salesman', back_populates='sales')
    customer = relationship('Customer', back_populates='sales')

Base.metadata.create_all(bind=engine)


# session creation
Session = sessionmaker(bind=engine)
session = Session()

salesman_1 = Salesman(name="John", surname="Doe")
salesman_2 = Salesman(name="Jane", surname="Smith")
salesman_3 = Salesman(name="Jim", surname="Beam")
salesman_4 = Salesman(name="Jack", surname="Daniels")
salesman_5 = Salesman(name="Jill", surname="Valentine")
salesman_6 = Salesman(name="Jerry", surname="Seinfeld")
salesman_7 = Salesman(name="Jessica", surname="Jones")
salesman_8 = Salesman(name="Joan", surname="Holloway")
salesman_9 = Salesman(name="Jacob", surname="Black")
salesman_10 = Salesman(name="Jared", surname="Leto")


customer_1 = Customer(cust_name="Alice", cust_surname="Johnson")
customer_2 = Customer(cust_name="Bob", cust_surname="Brown")
customer_3 = Customer(cust_name="Charlie", cust_surname="Davis")
customer_4 = Customer(cust_name="Diana", cust_surname="Evans")
customer_5 = Customer(cust_name="Eve", cust_surname="Wilson")
customer_6 = Customer(cust_name="Frank", cust_surname="Garcia")
customer_7 = Customer(cust_name="Grace", cust_surname="Miller")
customer_8 = Customer(cust_name="Hank", cust_surname="Moore")
customer_9 = Customer(cust_name="Ivy", cust_surname="Taylor")
customer_10 = Customer(cust_name="Jack", cust_surname="Anderson")


sale_1 = Sales(product="Product1", price=100)
sale_2 = Sales(product="Product2", price=200)
sale_3 = Sales(product="Product3", price=300)
sale_4 = Sales(product="Product4", price=400)
sale_5 = Sales(product="Product5", price=500)
sale_6 = Sales(product="Product6", price=600)
sale_7 = Sales(product="Product7", price=700)
sale_8 = Sales(product="Product8", price=800)
sale_9 = Sales(product="Product9", price=900)
sale_10 = Sales(product="Product10", price=1000)

salesmen = [salesman_1, salesman_2, salesman_3, salesman_4, salesman_5, salesman_6, salesman_7, salesman_8, salesman_9, salesman_10]
customers = [customer_1, customer_2, customer_3, customer_4, customer_5, customer_6, customer_7, customer_8, customer_9, customer_10]
sales = [sale_1, sale_2, sale_3, sale_4, sale_5, sale_6, sale_7, sale_8, sale_9, sale_10]

session.add_all(salesmen)
session.add_all(customers)
session.add_all(sales)
session.commit()

salesman_1.sales.append(sale_1)
salesman_2.sales.append(sale_2)
salesman_3.sales.append(sale_3)
salesman_4.sales.append(sale_4)
salesman_5.sales.append(sale_5)
salesman_6.sales.append(sale_6)
salesman_7.sales.append(sale_7)
salesman_8.sales.append(sale_8)
salesman_9.sales.append(sale_9)
salesman_10.sales.append(sale_10)


customer_1.sales.append(sale_1)
customer_2.sales.append(sale_2)
customer_3.sales.append(sale_3)
customer_4.sales.append(sale_4)
customer_5.sales.append(sale_5)
customer_6.sales.append(sale_6)
customer_7.sales.append(sale_7)
customer_8.sales.append(sale_8)
customer_9.sales.append(sale_9)
customer_10.sales.append(sale_10)


session.commit()

while True:

    tables = ["sales", "salesman", "customer"]

    print("Avaliable commands: ")
    print("0 - to exit")

    print("1 - Відображення усіх угод")
    print("2 - Відображення угод конкретного продавця")
    print("3 - Відображення максимальної за сумою угоди")
    print("4 - Відображення мінімальної за сумою угоди")
    print("5 - Відображення максимальної суми угоди для конкретного продавця")
    print("6 - Відображення мінімальної за сумою угоди для конкретного продавця")
    print("7 - Відображення максимальної за сумою угоди для конкретного покупця")
    print("8 - Відображення мінімальної за сумою угоди для конкретного покупця")

    print("9 - Відображення продавця з максимальною сумою продажів за всіма угодами")
    print("10 - Відображення продавця з мінімальною сумою продажів за всіма угодами")
    print("11 - Відображення покупця з максимальною сумою покупок за всіма угодами")
    print("12 - Відображення середньої суми покупки для конкретного покупця")
    print("13 - Відображення середньої суми покупки для конкретного продавця")


    command = int(input("Input your command: "))

    if command == 0:
        break

    elif command == 1:
        results = session.query(Sales).all()

        for result in results:
            print(result.product, result.price)


    elif command == 2:

        for salesman in session.query(Salesman).all():

            results = session.query(Sales).filter(Sales.salesman_id == salesman.id).all()

            if results:

                print(f"Sales for {salesman.name}:")

                for result in results:
                    print(f"Product: {result.product}, Price: {result.price}")

            else:

                print(f"No sales found for {salesman.name}.")

    elif command == 3:

        max_price_sale = session.query(Sales).order_by(Sales.price.desc()).first()

        if max_price_sale:
            print(f"Product: {max_price_sale.product}, Price: {max_price_sale.price}")
        else:
            print("No sales found.")

    elif command == 4:

        min_price_sale = session.query(Sales).order_by(Sales.price.asc()).first()

        if min_price_sale:
            print(f"Product: {min_price_sale.product}, Price: {min_price_sale.price}")
        else:
            print("No sales found.")


    elif command == 5:

        salesman_name = input("Input salesman's name: ").lower()
        max_price_for_salesman = session.query(func.max(Sales.price)).join(Salesman).filter(
            func.lower(Salesman.name) == salesman_name).scalar()

        if max_price_for_salesman:

            print(f"Max summ per saler {salesman_name}: {max_price_for_salesman}")

        else:

            print("No such saler")


    elif command == 6:

        salesman_name = input("Input salesman's name: ").lower()
        min_price_for_salesman = session.query(func.min(Sales.price)).join(Salesman).filter(
            func.lower(Salesman.name) == salesman_name).scalar()

        if min_price_for_salesman:

            print(f"Min. summ per saler {salesman_name}: {min_price_for_salesman}")

        else:

            print("No such saler")



    elif command == 7:

        customer_name = input("Input customer's name: ").lower()

        max_price_for_customer = session.query(func.max(Sales.price)).join(Customer).filter(

            func.lower(Customer.cust_name) == customer_name).scalar()

        if max_price_for_customer:

            print(f"Max summ per customer {customer_name}: {max_price_for_customer}")


        else:

            print("No such customer")



    elif command == 8:

        customer_name = input("Input customer's name: ").lower()

        min_price_for_customer = session.query(func.min(Sales.price)).join(Customer).filter(

            func.lower(Customer.cust_name) == customer_name).scalar()

        if min_price_for_customer:

            print(f"Min. summ per saler {customer_name}: {min_price_for_customer}")


        else:

            print("No such customer")



    elif command == 9:

        salesman_name = input("Input salesman's name: ").strip().lower()
        max_salesman = session.query(Salesman).join(Sales).group_by(Salesman.id).filter(

        func.lower(Salesman.name) == salesman_name).order_by(
        func.sum(Sales.price).desc()).first()

        total_sales_amount = sum(sale.price for sale in max_salesman.sales)

        print(f"The salesman with the maximum sales is {max_salesman.name} {max_salesman.surname}.")
        print(f"Total sales amount: {total_sales_amount}")


    elif command == 10:

        salesman_name = input("Input salesman's name: ").strip().lower()
        min_salesman = session.query(Salesman).join(Sales).group_by(Salesman.id).filter(

        func.lower(Salesman.name) == salesman_name).order_by(
        func.sum(Sales.price).asc()).first()

        total_sales_amount = sum(sale.price for sale in min_salesman.sales)

        print(f"The salesman with the minimum sales is {min_salesman.name} {min_salesman.surname}.")
        print(f"Total sales amount: {total_sales_amount}")


    elif command == 11:

        customer_name = input("Input customers's name: ").strip().lower()
        max_customer = session.query(Customer).join(Sales).group_by(Customer.id).filter(

        func.lower(Customer.cust_name) == customer_name).order_by(
        func.sum(Sales.price).asc()).first()

        total_sales_amount = sum(sale.price for sale in max_customer.sales)

        print(f"The customer with the minimum sales is {max_customer.cust_name} {max_customer.cust_surname}.")
        print(f"Total sales amount: {total_sales_amount}")


    elif command == 12:
        ...

    elif command == 13:
        ...

    else:
        print("Wrong command, try again")





