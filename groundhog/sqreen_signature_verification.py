import hmac
import hashlib

from flask import current_app

class SqreenSignatureVerification:

  def __init__(self, request_signature, request_body):

    self.signature = request_signature
    self.body = request_body
    self.secret = current_app.config["SQREEN_SECRET"].encode()

  def run(self):

    hasher = hmac.new(self.secret, self.body, hashlib.sha256)
    dig = hasher.hexdigest()
    return hmac.compare_digest(dig, self.signature)