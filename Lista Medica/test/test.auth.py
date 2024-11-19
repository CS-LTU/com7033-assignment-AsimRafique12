import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def test_user_registration(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'password': 'password123'
    })
    assert response.status_code == 200

def test_user_login(client):
    # Register user first
    client.post('/register', data={
        'username': 'testuser',
        'password': 'password123'
    })
    # Now test login
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'password123'
    })
    assert response.status_code == 200