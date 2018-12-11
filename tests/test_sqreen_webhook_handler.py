from unittest import TestCase
from unittest.mock import patch

from tests.test_main import app, test_client

from groundhog.sqreen_webhook_handler import SqreenWebhookHandler


class TestSqreenWebhookHandler(TestCase):
  def test_non_verified_alert_run(self):
    with patch('groundhog.sqreen_signature_verification', autospec=True) as mock_verification:
      with patch('groundhog.logger', autospec=True) as mock_logger:
        mock_logger.assert_called()
        
        mock_verification.return_value.run.return_value = False

        SqreenWebhookHandler({}).run()



