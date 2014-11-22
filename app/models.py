from app import db

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questionid = db.Column(db.Integer)
    datetime = db.Column(db.String(120))
    resp = db.Column(db.String(5000))

    def __repr__(self):
        return '<w/e>' % (self.nickname)