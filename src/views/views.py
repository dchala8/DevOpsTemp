from flask import request
from flask_restful import Resource
from src.models import Blacklist, BlacklistSchema

blacklist_schema = BlacklistSchema()
BEARER_TOKEN = "Bearer kfsdmxcvnms82439wwqeqe1sdfs5sdqe56"

class ViewBlacklist(Resource):

    def get(self, email:str):
        if 'Authorization' in request.headers:
            request_bearer_token = str(request.headers['Authorization'])
            if request_bearer_token != BEARER_TOKEN:
                return ("Not authorized"), 403
        else:
            return ("Must authenticate"), 400
        
        record = Blacklist.query.filter(Blacklist.email == email).first()
        if record is not None:
            return ({"is_in_black_list": True}), 200
        else:
            return ({"is_in_black_list": False}), 200
    
    