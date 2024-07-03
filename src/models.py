from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    client = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
 
    def __repr__(self):
        return f'{self.name}'