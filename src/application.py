from flask import Flask
from flask_restful import Api
from src.models import db
from src.views import (ViewBlacklist)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:devops1234@database-1.cyxrkg2exb5u.us-east-2.rds.amazonaws.com:5432/blacklist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(ViewBlacklist, '/blacklists/<string:email>')