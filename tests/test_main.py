import pytest
from unittest.mock import patch

from groundhog import create_app

@pytest.fixture
def app():
  app = create_app({
    'TESTING': True,
    'SQREEN_SECRET': 'some-string'
  })

  yield app

@pytest.fixture
def test_client(app):
  testing_client = app.test_client() 
  context = app.app_context()
  context.push()

  yield testing_client  

  context.pop()

def test_home(test_client):
  response = test_client.get('/', follow_redirects=True)
  assert response.status_code == 200


def test_receive_sqreen_alert(test_client):
  with patch('groundhog.sqreen_signature_verification', autospec=True) as mock_verification:
    with patch('groundhog.logger', autospec=True) as mock_logger:
      mock_verification.return_value.run.return_value = False
      mock_logger.return_value.run.return_value = False

      response = test_client.post(
        '/receive_sqreen_alert', 
        headers={ 'X-Sqreen-Integrity': 'some-string'}, 
        data={}, 
        follow_redirects=True
      )
      
      assert response.status_code == 200
