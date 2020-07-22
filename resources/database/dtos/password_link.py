from resources.database import db


class PasswordLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="password_links")

    def __init__(self, token, user):
        self.token = token
        self.user = user