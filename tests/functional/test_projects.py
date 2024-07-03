import pytest
from src.app import app, db
from src.models import Project

def test_select_project(client):
    projects = Project.query.all()
    for project in projects:
        response = client.get(f'/project/{project.id}')
        assert response.status_code == 200
        assert bytes(project.name, 'utf-8') in response.data
        assert bytes(project.client, 'utf-8') in response.data
        assert bytes(str(project.duration), 'utf-8') in response.data
    
def test_project_data_display_on_select_page(client):
    project = Project.query.first()
    
    response = client.get(f'/project/{project.id}')
    
    data = response.data.decode('utf-8')
    
    assert project.name in data
    assert project.client in data
    assert str(project.duration) in data