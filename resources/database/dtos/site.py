from resources.database import db


class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    proxy_pass_url = db.Column(db.Text, nullable=False)
    users = db.relationship("User", secondary="site_user_link", back_populates="sites")

    def __init__(self, name, proxy_pass_url):
        self.name = name
        self.proxy_pass_url = proxy_pass_url
