from datetime import datetime

from flask import url_for

from yacut import db
from .constants import (
    MAX_LENGTH_SHORT, MAX_LENGTH_ORIGINAL
)


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String(MAX_LENGTH_SHORT), unique=True, nullable=True)
    original = db.Column(db.String(MAX_LENGTH_ORIGINAL), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            short_link=url_for(
                'redirect_on_link',
                short_id=self.short,
                _external=True
            ),
            url=self.original,
        )
