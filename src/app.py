from flask import Flask
from src.views import main
from src.models import db
from flask_sqlalchemy import SQLAlchemy
from src.db_populate import get_data
 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db.init_app(app)
 
with app.app_context():
    db.create_all()
    projects = get_data()
    db.session.add_all(projects)
    db.session.commit()


app.register_blueprint(main)
 
if __name__ == '__main__':
    app.run(debug=True)