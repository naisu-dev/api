from flask import *
from ketsui import *
import random

webserver = Flask("api")

@webserver.route("/ketsui")
def main():
    return(number(random.randrange(1, 26, 1)))

webserver.run()