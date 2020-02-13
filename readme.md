# Lego Scraper

## Usage guide
1. clone repo repo
```sh
$ git clone https://github.com/oreilm49/lego-scraper.git
```
2. insure python 3 is installed on your machine
3. create a virtual environment
```sh
$ virtualenv venv
```
4. start env (windows)
```sh
$ source venv/scripts/activate
```
4. start env (unix)
```sh
$ source venv/bin/activate
```
5. chdir into app directory
```sh
$ cd lego-scraper/
```
6. install dependencies
```sh
pip install -r requirements.txt
```
7. set flask app environment variable
```sh
$ export FLASK_APP=main.py
```
8. initialize database
```sh
$ flask db init
$ flask db migrate
$ flask db upgrade
```
9. run flask app & Visit http://127.0.0.1:5000 in your browser to see it running.
```sh
$ python main.py
```

10. open a new console window and run scrapyd
```sh
$ source venv/scripts/activate
$ cd lego-scraper/app/scraper
$ scrapyd
```
11. open another console window, chdir into scrapy directory and deploy default scraper
```sh
$ source venv/scripts/activate
$ cd lego-scraper/app/scraper
$ scrapyd-deploy
```
12. Go to your browser and click Run bot to activate the scraper