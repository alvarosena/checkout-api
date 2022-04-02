import os
from flask import Flask
from models import db
from flask_migrate import Migrate 

from modules.buyers.buyer_controller import buyers

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(buyers, url_prefix='/api/v1')

@app.route('/')
def index():
    return {"message": "Hello, World"}
