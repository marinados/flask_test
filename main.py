import sqreen
sqreen.start()

from flask import Flask
from flask import render_template
from flask import request

from sqreen_signature_verification import SqreenSignatureVerification
from sqreen_report_dispatcher import SqreenReportDispatcher

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

@app.route('/')
def home():
  return 'ok'

@app.route('/receive_sqreen_alert', methods=['POST'])
def receive_sqreen_alert():

  request_body = request.get_data()
  request_signature = request.headers['X-Sqreen-Integrity']

  if SqreenSignatureVerification.run(request_signature, request_body):
    SqreenReportDispatcher.run(request.json)

  return 'ok'

# [:security_event, :pulse, :security_response, :test]


# to do
# tests
# alert management services (slack + log)