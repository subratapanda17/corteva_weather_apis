import pytest
from app import create_app

@pytest.fixture
def app():
   app = create_app()
   app.config.from_object('api.config.settings.TestingConfig')
   yield app

@pytest.fixture
def client(app):
   return app.test_client()


def test_weather_ingestion_success(client):
   response = client.get('/api/weatherIngestion/')

   assert response.status_code == 200
   data_sample = response.get_json().get('message')
   assert 'rows inserted' in data_sample

def test_weather_ingestion_conflict(client):
   response = client.get('/api/weatherIngestion/')

   assert response.status_code == 409
   data_sample = response.get_json().get('message')
   assert 'already present' in data_sample