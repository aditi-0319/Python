from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

url = "http://localhost:5000/"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
db = SQLAlchemy()
db.init_app(app)


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    quote = db.Column(db.String(1000), nullable=False)


with app.app_context():
    # db.create_all()
    # new_quote = Quote(id=1, name="Thomas A. Edison",
    #                   quote="Many of life’s failures are people who did not realize how close they were to success when they gave up.")
    # db.session.add(new_quote)
    db.session.commit()

    quotes = Quote.query.all()
    for quote in quotes:
        print(f'ID: {quote.id}   |    Name: {quote.name}   |     Quote: {quote.quote}')
