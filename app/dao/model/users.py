from marshmallow import Schema, fields
from  app.database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String(50))
    surname = db.Column(db.String)
    favorite_genre = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.String(required=True)
    password = fields.String()
    name = fields.String()
    surname = fields.String()
    favorite_genre = fields.String()

