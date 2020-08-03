from resources.database import db


class SiteCustomHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header_name = db.Column(db.Text, nullable=False)
    header_content = db.Column(db.Text, nullable=True)

    site_id = db.Column(db.Integer, db.ForeignKey("site.id"))
    site = db.relationship("Site", back_populates="custom_headers")

    def __init__(self, header_name, header_content, site):
        self.header_name = header_name
        self.header_content = header_content
        self.site = site
