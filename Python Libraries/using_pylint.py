"""
This file contains the definition of our Flask application.
It's also run the app
"""

from flask import Flask

APP = Flask(__name__)

if __name__ == "__main__":
    APP.run()