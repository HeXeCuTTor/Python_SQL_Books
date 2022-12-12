import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher,Shop,Book, Stock, Sale

DSN = "postgresql://postgres:postgres@localhost:5432/myhomework"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# publisher1 = Publisher(name="Author_1")
# publisher2 = Publisher(name="Author_2")
# session.add_all([publisher1,publisher2])
# session.commit()

# shop1 = Shop(name='Shop_1')
# shop2 = Shop(name='Shop_2')
# session.add_all([shop1,shop2])
# session.commit()

# book1 = Book(title="Book_1", publisher_id = '1')
# book2 = Book(title="Book_2", publisher_id = '1')
# book3 = Book(title="Book_3", publisher_id = '2')
# book4 = Book(title="Book_4", publisher_id = '2')
# session.add_all([book1,book2,book3,book4])
# session.commit()

# stock1 = Stock(id='1',book_id='1',shop_id='1',count='5')
# stock2 = Stock(id='2',book_id='2',shop_id='1',count='6')
# stock3 = Stock(id='3',book_id='3',shop_id='2',count='7')
# stock4 = Stock(id='4',book_id='4',shop_id='2',count='4')
# stock5 = Stock(id='5',book_id='1',shop_id='2',count='8')
# stock6 = Stock(id='6',book_id='3',shop_id='1',count='9')
# session.add_all([stock1,stock2,stock3,stock4,stock5,stock6])
# session.commit()

# sale1 = Sale(id='1',price='100', date_sale= '09/11/2020',stock_id='1')
# sale2 = Sale(id='2',price='500', date_sale= '11/03/2019',stock_id='2')
# sale3 = Sale(id='3',price='300', date_sale= '16/07/2018',stock_id='3')
# sale4 = Sale(id='4',price='600', date_sale= '27/12/2021',stock_id='4')
# sale5 = Sale(id='5',price='1200', date_sale= '04/05/2011',stock_id='5')
# sale6 = Sale(id='6',price='400', date_sale= '19/09/2015',stock_id='6')
# session.add_all([sale1,sale2,sale3,sale4,sale5,sale6])
# session.commit()

name = input("Введите имя автора: ")
query = session.query(Stock,Book.title,Shop.name,Sale.price,Sale.date_sale)
query = query.join(Sale)
query = query.join(Shop)
query = query.join(Book)
query = query.join(Publisher)
records = query.filter(Publisher.name == (name))
for c in records:
    print(f'Название книги: {c[1]}, Магазин: {c[2]}, Стоимость: {c[3]}, Дата покупки: {(c[4]).day}-{(c[4]).month}-{(c[4]).year}')

session.close()