import os
from flask import Flask
from models import db
from flask_migrate import Migrate 

from modules.buyers.buyer_controller import buyers
from modules.cards.card_controller import cards
from modules.payments.payment_controller import payments

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(buyers, url_prefix='/api/v1')
app.register_blueprint(cards, url_prefix='/api/v1')
app.register_blueprint(payments, url_prefix='/api/v1')