from flask_sqlalchemy import Model, SQLAlchemy
import datetime
from sqlalchemy import Column, String, DateTime, Integer
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Blacklist(Model):
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    app_uuid = Column(String(50))
    blockd_reason = Column(String(255))
    client_ip = Column(String(50))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class BlacklistSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Blacklist
        include_relationships = True
        include_fk = True
        load_instance = True

    email = fields.String()
    app_uuid = fields.String()
    blockd_reason = fields.String()
    client_ip = fields.String()
    timestamp = fields.DateTime()