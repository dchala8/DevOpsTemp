from flask_sqlalchemy import  SQLAlchemy
import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Blacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    app_uuid = db.Column(db.String(50))
    blocked_reason = db.Column(db.String(255))
    client_ip = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class BlacklistSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: Blacklist
        include_relationships = True
        load_instance = True