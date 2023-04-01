from decimal import Decimal
from http.client import NOT_FOUND
from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
import datetime
from POST.models import db, Blacklist, BlacklistSchema


blacklist_schema = BlacklistSchema()

class ViewBlacklist(Resource):

    def post(self,):
        if request.method=='POST':
            newBlacklist = Blacklist(email = request.json.get("email"),
                                     app_uuid = request.json.get("app_uuid"),
                                     blockd_reason = request.json.get("blocked_reason"),
                                     client_ip = request.remote_addr)
            db.session.add(newBlacklist)
            return {"Code": "200", "message": "blakclist created"}, 200
        else:
            return {"status_code": "404", "message": "not exists post with provided id"}, 404