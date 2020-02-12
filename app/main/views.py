from . import main
from flask import render_template
from app.models import Lego

@main.route('/')
def home():
   products = Lego.query.all()
   return render_template('index.html', products=products)