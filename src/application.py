from flask import Flask
from flask_restful import Api
from models import db
from views import (ViewBlacklist,ViewBlacklistGet)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:devops1234@database-blacklist.cyxrkg2exb5u.us-east-2.rds.amazonaws.com:5432/blacklist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(ViewBlacklistGet, '/blacklists/<string:email>')
api.add_resource(ViewBlacklist, '/blacklists')

if __name__ == "__main__":
    app.run(port = 5000, debug = True)