from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(150), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)

    def from_dict(self, data):
        values = list(data.values())
        i = 0
        for field in ['original', 'short']:
            setattr(self, field, values[i])
            i += 1

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_view',
                short_id=self.short,
                _external=True
            )
        )
