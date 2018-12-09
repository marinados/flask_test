from flask import Flask
from flask import render_template
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

from sqreen_signature_verification import SqreenSignatureVerification
from sqreen_report_dispatcher import SqreenReportDispatcher
from logger import Logger

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
sqreen.start()

@app.route('/')
def home():
  return 'ok'

@app.route('/receive_sqreen_alert', methods=['POST'])
def receive_sqreen_alert():

  request_body = request.get_data()
  request_signature = request.headers['X-Sqreen-Integrity']

  if SqreenSignatureVerification(request_signature, request_body).run():
    SqreenReportDispatcher(request.json).run()
  else:
    Logger("suspicious alert pretending to be Sqreen detected")

  return 'ok'
