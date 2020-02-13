from app import db
from sqlalchemy.sql import func
import datetime

class Lego(db.Model):
    __tablename__='lego'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(255))
    name = db.Column(db.String(255))
    price = db.Column(db.String(255))
    description = db.Column(db.Text())
    rating = db.Column(db.String(255))
    available = db.Column(db.String(255))
    updated = db.Column(db.DateTime(), onupdate=func.now())

    def __init__(
            self, model=None, name=None, price=None,
            description=None, rating=None, available=None
        ):
        self.model = model
        self.name = name
        self.price = price
        self.description = description
        self.rating = rating
        self.available = available

    def json(self):
        output = {}
        output['id'] = self.id
        output['model'] = self.model
        output['name'] = self.name
        output['price'] = self.price
        output['description'] = self.description
        output['rating'] = self.rating
        output['available'] = self.available
        if self.updated:
            output['updated'] = self.updated.strftime("%m/%d/%Y, %H:%M:%S")
        return output