from . import main

@main.route('/')
def home():
   return "hello world!"