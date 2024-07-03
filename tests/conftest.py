import pytest
from src.app import app, db
from src.models import Project

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite3:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            project1 = Project(name='Website Redesign', client='Tech Solutions Inc.', duration=15)
            project2 = Project(name='Mobile App Development', client='Innovative Apps LLC', duration=30)
            db.session.add_all([project1, project2])
            db.session.commit()
            yield client
            db.drop_all()
            
            