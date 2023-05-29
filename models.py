import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "Publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    publisher = relationship("Publisher", back_populates="book")

class Book(Base):
    __tablename__ = "Book"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    book = relationship("Book", back_populates="Publisher")

class Shop(Base):
    __tablename__ = "Shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    shop = relationship("shop", back_populates="course")


class Stock(Base):
    __tablename__ = "Stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, nullable=False)
    id_shop = sq.Column(sq.Integer, nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    # course = relationship(Course, back_populates="homeworks")
    stock = relationship(Course, backref="homeworks")

class Sale(Base):
    __tablename__ = "Sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sale = sq.Column(sq.Text, nullable=False)
    id_stock = sq.Column(sq.Integer, nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    # course = relationship(Course, back_populates="homeworks")
    sale = relationship(Course, backref="homeworks")


def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


from models import create_tables, Publisher, Shop, Book, Stock, Sale


DSN = "postgresql://postgres:postgres@localhost:5432/netology_db"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()

# создание объектов
 = Course(name="JavaScript")
print(js.id)
hw1 = Homework(number=1, description="первое задание", course=js)
hw2 = Homework(number=2, description="второе задание (сложное)", course=js)

session.add(js)
print(js.id)
session.add_all([hw1, hw2])
session.commit()  # фиксируем изменения
print(js.id)