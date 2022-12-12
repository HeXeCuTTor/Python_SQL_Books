import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=80), unique=True)

    def __str__(self):
        return f'{self.id}: {self.name}'

class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=80))

    def __str__(self):
        return f'{self.id}: {self.name}'

class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.Text, nullable=False)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="book")

    def __str__(self):
        return f'{self.id}: {self.title}, {self.publisher_id}'

class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True, unique=True)
    count = sq.Column(sq.Integer, nullable=False)
    book_id = sq.Column(sq.Integer, sq.ForeignKey("book.id"), primary_key=True, nullable=False)
    shop_id = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), primary_key=True,nullable=False)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")

    def __str__(self):
        return f'{self.id}: {self.count}, {self.book_id}, {self.shop_id}'


class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)

    stock = relationship(Stock, backref="sale")

    def __str__(self):
        return f'{self.id}: {self.price}, {self.date_sale}, {self.stock_id}'    

def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)





    

