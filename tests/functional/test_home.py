import pytest
from src.app import app, db
from src.models import Project

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Select' in response.data

def test_project_data_display_on_home_page(client):
    response = client.get('/')
    data = response.data.decode('utf-8')
    
    assert 'Website Redesign' in data
    assert 'Mobile App Development' in data