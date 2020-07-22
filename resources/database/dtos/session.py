from resources.database import db


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="sessions")

    def __init__(self, token, user):
        self.token = token
        self.user = user
