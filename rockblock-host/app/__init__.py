from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # create the application instance :)
app.config.from_object("config")
db = SQLAlchemy(app)

import views, models