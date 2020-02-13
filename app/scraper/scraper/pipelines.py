import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Text, Integer, DateTime
from sqlalchemy.sql import func
import datetime

basedir = os.getcwd().split('\\app')[0]
DeclarativeBase = declarative_base()


class Lego(DeclarativeBase):
    __tablename__='lego'
    id = Column(Integer, primary_key=True)
    model = Column(String(255))
    name = Column(String(255))
    price = Column(String(255))
    description = Column(Text())
    rating = Column(String(255))
    updated = Column(DateTime(), onupdate=func.now())

    def __init__(
            self, model=None, name=None, price=None,
            description=None, rating=None, available=None,
            updated=None
        ):
        self.model = model
        self.name = name
        self.price = price
        self.description = description
        self.rating = rating
        self.available = available
        self.updated = updated


class LegoPipeline(object):


    def __init__(self):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)
        self.conn = self.engine.connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def process_item(self, item, spider):
        lego = self.session.query(Lego).filter_by(model=item['model']).first()
        if not lego:
            lego = Lego(
                model=item['model'],
                name=item['name'],
                price=item['price'],
                description=item['description'],
                rating=item['rating'],
                available=item['available'],
                updated=datetime.datetime.now()
            )
            self.session.add(lego)
            self.session.commit()
        else:
            lego.model = item['model']
            lego.name = item['name']
            lego.price = item['price']
            lego.description = item['description']
            lego.rating = item['rating']
            lego.available = item['available'],
            lego.updated = datetime.datetime.now()
            self.session.commit()
