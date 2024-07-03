import pytest
from src.db_populate import get_data
from src.models import Project

def test_data_load(client):
    data = [
        Project(name='Website Redesign', client='Tech Solutions Inc.', duration=15),
        Project(name='Mobile App Development', client='Innovative Apps LLC', duration=30),
        Project(name='Cloud Migration', client='Cloud Services Co', duration=12),
        Project(name='Data Analysis Project', client='Analytics R Us', duration=30),
        Project(name='E-commerce Platform', client='Online Retailers Ltd', duration=96),
        ]
    retrieved_data = get_data()
    
    print(f"Retrieved data: '{retrieved_data[0]}'")
    print(f"Item: '{data[0]}'")
    assert len(data) == len(retrieved_data)
    for d, rd in zip(data, retrieved_data):
        assert d.name == rd.name
        assert d.client == rd.client
        assert d.duration == rd.duration