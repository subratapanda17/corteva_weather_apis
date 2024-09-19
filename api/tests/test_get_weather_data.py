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


def test_all_data(client):
   response = client.get('/api/getWeatherData/')
   
   assert response.status_code == 200
   data_sample = response.get_json().get('data')[0]
   assert 'maxtemp' in data_sample
   assert 'mintemp' in data_sample
   assert 'rainfall' in data_sample
   assert 'date' in data_sample

def test_with_params(client):
   response = client.get('/api/getWeatherData/', query_string={
      'date': 19850102,
      'weather_station_id': 'USC00134735',
      'page_no': 1
   })
   assert response.status_code == 200
   data_sample = response.get_json().get('data')[0]
   assert 'maxtemp' in data_sample
   assert 'mintemp' in data_sample
   assert 'rainfall' in data_sample
   assert 'date' in data_sample

def test_with_wrong_params(client):
   response = client.get('/api/getWeatherData/', query_string={
      'a': 19850102,
      'b': 'USC00134735',
      'c': 1
   })
   assert response.status_code == 400
   data_sample = response.get_json().get('error')
   assert 'Unknown arguments' in data_sample

def test_with_wrong_values(client):
   response = client.get('/api/getWeatherData/', query_string={
      'date': 20240403,
      'weather_station_id': 'NON_EXISTING_CODE',
      'page_no': 1
   })
   assert response.status_code == 404
   data_sample = response.get_json().get('message')
   assert 'no record' in data_sample

def test_with_wrong_page_no(client):
   response = client.get('/api/getWeatherData/', query_string={
      'page_no': -11
   })
   assert response.status_code == 400
   data_sample = response.get_json().get('message')
   assert 'positive integer' in data_sample