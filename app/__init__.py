from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.Develop")

db = SQLAlchemy(app)
#db.create_all();

from app import views
from app.models import light_states