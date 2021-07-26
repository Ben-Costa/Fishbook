from flask import Flask

app = Flask(__name__, static_folder="../FishBookApp/static")

from FishBookApp import routes