from resources.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=True)
    salt = db.Column(db.Text, nullable=True)
    admin = db.Column(db.Boolean, nullable=False)
    sites = db.relationship("Site", secondary="site_user_link", back_populates="users")
    sessions = db.relationship("Session", back_populates="user")
    password_links = db.relationship("PasswordLink", back_populates="user")

    def __init__(self, name, password, salt, admin=False):
        self.name = name
        self.password = password
        self.salt = salt
        self.admin = admin
