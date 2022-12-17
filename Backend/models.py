from click import password_option
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class User(db.Model):
    __tablename__='User'
    user_id     =       db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name   =       db.Column(db.String(100))
    password    =       db.Column(db.String(200))
    first_name  =       db.Column(db.String(40))
    middle_name =       db.Column(db.String(40))
    last_name   =       db.Column(db.String(40))
    dob         =       db.Column(db.DateTime)
    email       =       db.Column(db.String(60))
    roll_number =       db.Column(db.String(40))
    role        =       db.Column(db.String)
    created_at  =       db.Column(db.DateTime(), default=db.func.now())

class Post(db.Model):
    __tablename__='Post'
    user_id     =   db.Column(db.ForeignKey('User.user_id'))
    post_id     =   db.Column(db.Integer,primary_key=True, autoincrement=True)
    text        =   db.Column(db.BLOB)
    created_at  =   db.Column(db.DateTime, default=db.func.now())
    likes       =   db.Column(db.Integer)
