from flask import Flask
from flask_restful import Api
from models import db
from views import (ViewBlacklist,ViewBlacklistGet,ViewBlacklistHealth)

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:devops1234@database-blacklist.cyxrkg2exb5u.us-east-2.rds.amazonaws.com:5432/blacklist'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['PROPAGATE_EXCEPTIONS'] = True

app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()

api = Api(application)
api.add_resource(ViewBlacklistGet, '/blacklists/<string:email>')
api.add_resource(ViewBlacklist, '/blacklists')
api.add_resource(ViewBlacklistHealth, '/')

if __name__ == "__main__":
    application.run(port = 5000, debug = True, host='0.0.0.0')