from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SECRET_KEY'] = 'b1306c9f18a7260a8397e391eb5d6284'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form.db'

db = SQLAlchemy(app)

from website import routes