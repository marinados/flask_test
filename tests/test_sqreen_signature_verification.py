import pytest
import unittest.mock as mock
import hmac
import hashlib


from tests.test_main import app, test_client
from groundhog.sqreen_signature_verification import SqreenSignatureVerification

def test_failed_verification_run(test_client):
  signature = 'blablabla'
  body = b'random_string'
  assert SqreenSignatureVerification(signature, body).run() == False

def test_successful_verification_run(test_client):
  # secret key being 'some-string'
  body = b'request_body'
  signature = hmac.new(b'some-string', body, hashlib.sha256).hexdigest()
  assert SqreenSignatureVerification(signature, body).run() == True