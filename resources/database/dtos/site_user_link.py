from resources.database import db


class SiteUserLink(db.Model):
    __tablename__ = "site_user_link"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey("site.id"), primary_key=True)
