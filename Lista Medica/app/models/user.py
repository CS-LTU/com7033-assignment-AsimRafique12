from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    _tablename_ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def _repr_(self):
        return f'<User {self.username}>'