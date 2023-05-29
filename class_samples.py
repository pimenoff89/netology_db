import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale


DSN = "postgresql://postgres:postgres@localhost:5432/netology_db"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()

# создание объектов
publisher_one = Publisher(name="Publisher_one")
publisher_two = Publisher(name="Publisher_two")
publisher_three = Publisher(name="Publisher_three")

book_one = Book(name="The call of the wild", id_publisher=1)
book_two = Book(name="Harry Potter", id_publisher=2)
book_three = Book(name="Atlant Shrugged", id_publisher=3)

shop_one = Shop(name="Book Store")
shop_two = Shop(name="The Super Book Store")
shop_three = Shop(name="The Mega Book Store")

big_stock = Stock(id_book=1, id_shop=1, count=1250)
small_stock = Stock(id_book=2, id_shop=2, count=250)
moderate_stock = Stock(id_book=3, id_shop=3, count=750)

big_sale = Sale(price=1, date_sale=17 april 1985, id_stock=1, count=50)
new_year_sale = Sale(price=2, date_sale=17 may 1995, id_stock=2, count=250)
mega_sale = Sale(price=3, date_sale=17 june 1975, id_stock=3, count=350)

session.add_all([publisher_one, publisher_two, publisher_three, book_one, book_two, book_three, shop_one, shop_two, shop_three, big_stock, small_stock, moderate_stock,
                 big_sale, new_year_sale, mega_sale])


session.commit()  # фиксируем изменения
