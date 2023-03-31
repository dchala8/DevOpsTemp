from decimal import Decimal
from http.client import NOT_FOUND
from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
import datetime
from models import db, Blacklist, BlacklistSchema


blacklist_schema = BlacklistSchema()

class ViewBlacklist(Resource):

    def get(self, email):
        record = Blacklist.query.filter(Blacklist.email == email).first()
        return blacklist_schema.dump(record)
    
    