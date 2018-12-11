from flask import Flask
from flask import request
from logging.config import dictConfig

import sqreen

dictConfig({
    'version': 1,
    'formatters': { 
      'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
      'console': {
        'class' : 'logging.StreamHandler',
        'formatter': 'default',
        'level'   : 'INFO',
        'stream'  : 'ext://sys.stdout'},
      'file': {
        'class' : 'logging.handlers.RotatingFileHandler',
        'formatter': 'default',
        'filename': 'logs/applog.log',
        'level': 'WARNING'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config = True)

  if test_config is None:
    app.config.from_pyfile('config.py', silent=True)
  else:
    app.config.from_mapping(test_config)

  sqreen.start()
  
  @app.route('/')
  def home():
    return 'ok'

  from groundhog import sqreen_webhook_handler
  app.register_blueprint(sqreen_webhook_handler.bp)

  app.add_url_rule('/', endpoint='receive_sqreen_alert')

  return app


