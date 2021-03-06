from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # create the application instance :)
app.config.from_object("config")
db = SQLAlchemy(app)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/romaeris_host.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('Romaeris host startup')

import views, models
