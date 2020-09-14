from website import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    datasets = db.relationship('Dataset', backref='author', lazy=True)
    
    def __repr__(self):
        return f"Username: {self.username}"

class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rm = db.Column(db.Float, nullable=False)
    o = db.Column(db.Float, nullable=False)
    ps = db.Column(db.Float, nullable=False)
    ad = db.Column(db.Float, nullable=False)
        