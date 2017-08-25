import os

SECRET_KEY = "you-will-never-guess"

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

'Create Schema with Utf8.asdfadsf'
#SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:raspberry@192.168.1.100:3306/SatTestDB'

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False