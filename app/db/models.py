from flask_login import UserMixin

from app.extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, index=True)
    sub = db.Column(db.String, unique=True, index=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False, index=True)
    profile_pic = db.Column(db.String)

    @classmethod
    def get(cls, sub):
        user = cls.query.filter_by(sub=sub).first()
        if not user:
            return None

        return user

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj
