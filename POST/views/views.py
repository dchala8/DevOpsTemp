from flask import request
from flask_sqlalchemy import Model, SQLAlchemy
import datetime 
from flask_restful import Resource
from POST.models import db, Blacklist, BlacklistSchema

blacklist_schema = BlacklistSchema()
BEARER_TOKEN = "Bearer kfsdmxcvnms82439wwqeqe1sdfs5sdqe56"

class ViewBlacklist(Resource):

    def post(self,):
        if 'Authorization' in request.headers:
            request_bearer_token = str(request.headers['Authorization'])
            if request_bearer_token != BEARER_TOKEN:
                return ("Not authorized"), 403
        else:
            return ("Must authenticate"), 400
        
        if request.method=='POST' and request.json is not None:
            if 'email' in request.json and 'app_uuid' in request.json and 'blocked_reason' in request.json:
                newBlacklist = Blacklist(email = request.json.get("email"),
                                        app_uuid = request.json.get("app_uuid"),
                                        blockd_reason = request.json.get("blocked_reason"),
                                        timestamp = datetime.datetime.utcnow,
                                        client_ip = request.remote_addr)
                db.session.add(newBlacklist)
                return {"Code": "200", "message": "blakclist created"}, 200
            else:
                return {"status_code": "400", "message": ""}, 400
        else:
            return {"status_code": "404", "message": "NOT FOUND"}, 404