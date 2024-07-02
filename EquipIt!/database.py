from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///signup.db'
db = SQLAlchemy()
db.init_app(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(300), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)


with app.app_context():
    db.create_all()

    # Check if the user already exists
    # existing_user = Data.query.filter_by(username="Thomas").first()

    # if existing_user:
    #     # Update the existing user's password
    #     existing_user.password = "NewPassword123"
    #     db.session.commit()
    # else:
        # Insert a new user if the username doesn't exist
    new_user = Data(id=2, username="Alpa", password="MshJGc354")
    db.session.add(new_user)
    db.session.commit()

    users = Data.query.all()
    for user in users:
        print(f'ID: {user.id}   |    Name: {user.username}   |     Password: {user.password}')
