from datetime import datetime
from settings import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Todo %r, id %s>' % (self.name, self.id)

    def update(self, args):
        for key, value in args.items():
            setattr(self, key, value)
        db.session.commit()
        return self
