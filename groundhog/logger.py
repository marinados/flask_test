from flask import current_app

class Logger:

  def __init__(self, message):
    self.message = message

  def run(self):
    current_app.logger.warning(self.message)