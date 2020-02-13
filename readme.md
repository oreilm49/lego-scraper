# Lego Scraper

## Usage guide
1. insure python 3 is installed on your machine
2. create a virtual environment
`$ virtualenv venv`
`$ source venv/bin/activate`
3. install dependencies
`pip install -r requirements.txt`
4. set flask app environment variable
`$ export FLASK_APP=main.py`
5. build migrations repository
`$ flask db init`
6. create migrations script from models structure
`$ flask db migrate`
7. build tables from migration script
`$ flask db upgrade`
8. eggify scraper and deploy to scrapyd
`$ scrapyd-deploy`
9. schedule job (if running on windows, ensure pywin is installed)
`$ curl http://localhost:6800/schedule.json -d project=scraper -d spider=lego`