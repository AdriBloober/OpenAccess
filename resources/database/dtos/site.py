from resources.database import db


class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    host = db.Column(db.Text, nullable=False)
    proxy_pass_url = db.Column(db.Text, nullable=False)
    users = db.relationship("User", secondary="site_user_link", back_populates="sites")
    custom_headers = db.relationship("SiteCustomHeader", back_populates="site")

    def __init__(self, name, host, proxy_pass_url):
        self.name = name
        self.host = host
        self.proxy_pass_url = proxy_pass_url
