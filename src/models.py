from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

class Buyer(db.Model):
    __tablename__ = 'buyers'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(180), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    cards = db.relationship('Card')
    payments = db.relationship('Payment')
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    holder_name = db.Column(db.String, nullable=False)
    card_number = db.Column(db.String, nullable=False)
    expiration_date = db.Column(db.String, nullable=False)
    cvv = db.Column(db.Integer, unique=True, nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyers.id'))
    payments = db.relationship('Payment')
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String, nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyers.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    