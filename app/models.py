from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    secure_password = db.Column(db.String(255), nullable=False)
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvote', backref='user', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='user', lazy='dynamic')
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String) 