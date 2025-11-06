from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, Book
from forms import BookForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()
