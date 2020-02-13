# Lego Scraper

## Usage guide
1. clone repo repo
`$ git clone https://github.com/oreilm49/lego-scraper.git`
1. insure python 3 is installed on your machine
2. create a virtual environment
`$ virtualenv venv`
3. start env (windows)
`$ source venv/scripts/activate`
3. start env (unix)
`$ source venv/bin/activate`
3. chdir into app directory
`$ cd lego-scraper/`
4. install dependencies
`pip install -r requirements.txt`
5. set flask app environment variable
`$ export FLASK_APP=main.py`
6. initialize database
`$ flask db init`
`$ flask db migrate`
`$ flask db upgrade`
7. run flask app
`$ python main.py`
Visit http://127.0.0.1:5000 in your browser to see it running.
8. open a new console window and run scrapyd
`$ source venv/scripts/activate`
`$ cd lego-scraper/app/scraper`
`$ scrapyd`
9. open another console window, chdir into scrapy directory and deploy default scraper
`$ source venv/scripts/activate`
`$ cd lego-scraper/app/scraper`
`$ scrapyd-deploy`
10. Go to your browser and click Run bot to activate the scraper