import os
from app.app.models import Lego
from sqlalchemy.orm import sessionmaker
basedir = os.path.abspath(os.path.dirname(__file__))


class LegoPipeline(object):


    def __init__(self):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)
        self.conn = engine.connect()
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
