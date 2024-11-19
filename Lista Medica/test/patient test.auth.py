import pytest
from app import create_app, mongo

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app

def test_create_patient(client):
    response = client.post('/patients/create', data={
        'patient_id': '123',
        'age': 45,
        'gender': 'Male',
        'medical_data': {'hypertension': True}
    })
    assert response.status_code == 200