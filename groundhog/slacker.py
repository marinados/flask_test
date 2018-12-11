import requests
import json
from flask import current_app

class Slacker:

  headers = { 'Content-type': 'application/json' }

  def __init__(self, message):
    self.channel = current_app.config["SLACK_NOTIFICATION_CHANNEL"]
    self.message = message
    self.webhook_url = current_app.config["SLACK_WEBHOOK_URL"]

  def run(self):
    requests.post(
      self.webhook_url, 
      headers = self.headers,
      data = self.payload()
    )


  def payload(self):
    payload = { 
      'text': self.message, 
      'channel': self.channel
    }
    return json.dumps(payload)    
