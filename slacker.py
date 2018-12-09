import requests
import json
from flask import current_app

class Slacker:

  def __init__(self, message):
    self.message = message
    self.config = current_app.config

  def run(self):
    requests.post(
      self.config["SLACK_WEBHOOK_URL"], 
      data = self.payload(), 
      headers = self.headers()
    )


  def payload(self):
    payload = { 
      'text': self.message, 
      'channel': self.config["SLACK_NOTIFICATION_CHANNEL"]
    }
    return json.dumps(payload)

  def headers(self):
    { 'Content-type': 'application/json' }
