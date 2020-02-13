import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Text, Integer, DateTime
import datetime

basedir = 'C:\\Users\\marko\\OneDrive\\DOCUME~1\\09-LEG~1\\'
DeclarativeBase = declarative_base()


class Lego(DeclarativeBase):
    __tablename__='lego'
    id = Column(Integer, primary_key=True)
    model = Column(String(255))
    name = Column(String(255))
    price = Column(String(255))
    description = Column(Text())
    rating = Column(String(255))
    updated = Column(DateTime())

    def __init__(
            self, model=None, name=None, price=None,
            description=None, rating=None, available=None,
            updated=None
        ):
        model = self.model
        name = self.name
        price = self.price
        description = self.description
        rating = self.rating
        available = self.available
        updated = self.update


class LegoPipeline(object):


    def __init__(self):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)
        self.conn = self.engine.connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def process_item(self, item, spider):
        lego = Lego(
            model=item['model'],
            name=item['name'],
            price=item['price'],
            description=item['description'],
            rating=item['rating'],
            available=item['available']
        )
        self.session.add(lego)
        self.session.commit()
