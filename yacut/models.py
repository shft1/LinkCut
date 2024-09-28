from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(150), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)

    def from_dict(self, data):
        for field, value in [
            ('original', data['url']),
            ('short', data['custom_id'])
        ]:
            setattr(self, field, value)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_view',
                short_id=self.short,
                _external=True
            )
        )
