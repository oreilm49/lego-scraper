from . import main
from flask import render_template, jsonify, request
from app import db
from app.models import Lego
import requests
import os


@main.route('/', methods=['GET'])
def home():
   products = Lego.query.all()
   return render_template('index.html', products=products)


@main.route('/bot/jobs/', methods=['GET'])
def bot_jobs():
   # base_url = os.environ.get('URL') or 'http://127.0.0.1/'
   base_url = 'http://127.0.0.1'
   jobs_url = base_url+':6800/listjobs.json?project=scraper'
   r = requests.get(jobs_url, verify=False)
   if r.status_code == 200:
      response = jsonify(r.json()), 200
      return response
   response = jsonify({'message':'error retrieving jobs'}), r.status_code
   return response

@main.route('/bot/jobs/run')
def run_bot():
   # base_url = os.environ.get('URL') or 'http://127.0.0.1/'
   base_url = 'http://127.0.0.1'
   jobs_url = base_url+':6800/schedule.json -d project=scraper -d spider=lego'
   r = requests.get(jobs_url, verify=False)
   if r.status_code == 200:
      response = jsonify(r.json()), 200
      return response
   response = jsonify({'message':'error running job'}), r.status_code
   return response

@main.route('/lego', methods=['GET','DELETE'])
def lego():
   if request.method == 'GET':
      products = Lego.query.all()
      products = [p.json() for p in products]
      response = jsonify(products)
      return response
   if request.method == 'DELETE':
      Lego.query.delete()
      db.session.commit()
      response = jsonify({'message':'Lego data deleted'}), 201
      return response
