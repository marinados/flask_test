import hmac
import hashlib

from flask import current_app

class SqreenSignatureVerification:

  def run(request_signature, request_body):
    secret = current_app.config["SQREEN_SECRET"].encode()

    hasher = hmac.new(secret, request_body, hashlib.sha256)
    dig = hasher.hexdigest()
    return hmac.compare_digest(dig, request_signature)