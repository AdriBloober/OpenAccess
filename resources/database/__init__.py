from flask_sqlalchemy import SQLAlchemy

from resources import app

db = SQLAlchemy(app)


def setup():
    from resources.database.dtos import site_user_link, user, site, session, password_link

    db.create_all()


def add(obj):
    db.session.add(obj)
    db.session.commit()


def remove(obj):
    db.session.delete(obj)
    db.session.commit()
