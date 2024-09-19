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


def test_with_year_valid(client):
   response = client.get('/api/getWeatherStats/', query_string={
      'year': 1985,
   })
   assert response.status_code == 200
   data_sample = response.get_json().get('data')[0]
   assert 'average_max_temp' in data_sample
   assert 'average_min_temp' in data_sample
   assert 'total_precipitation_cm' in data_sample

def test_with_params_valid(client):
   response = client.get('/api/getWeatherStats/', query_string={
      'year': 1985,
      'weather_station_id': 'USC00110187'
   })
   assert response.status_code == 200
   data_sample = response.get_json().get('data')[0]
   assert 'average_max_temp' in data_sample
   assert 'average_min_temp' in data_sample
   assert 'total_precipitation_cm' in data_sample

def test_with_values_invalid(client):
   response = client.get('/api/getWeatherStats/', query_string={
      'year': 1918,
      'weather_station_id': 'INVALID_STATION_ID'
   })
   assert response.status_code == 404
   data_sample = response.get_json().get('message')
   assert 'No data' in data_sample

def test_with_params_invalid(client):
   response = client.get('/api/getWeatherStats/', query_string={
      'year': 1918,
      'wst': 'INVALID_STATION_ID'
   })
   assert response.status_code == 400
   data_sample = response.get_json().get('error')
   assert 'Unknown arguments' in data_sample

def test_with_params_none(client):
   response = client.get('/api/getWeatherStats/')
   assert response.status_code == 400
   data_sample = response.get_json().get('error')
   assert 'could not understand' in data_sample