from app import db
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
    updated = db.Column(db.DateTime())

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

    def json(self):
        output = {}
        output['id'] = self.id
        output['model'] = self.model
        output['name'] = self.name
        output['price'] = self.price
        output['description'] = self.description
        output['rating'] = self.rating
        output['available'] = self.available
        output['updated'] = self.updated.strftime("%m/%d/%Y, %H:%M:%S")
        return output