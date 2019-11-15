from app import db


class Var(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    val = db.Column(db.String(64))

    def __repr__(self):
        return '<Var {}>'.format(self.name)
