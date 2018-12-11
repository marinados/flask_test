from flask import (Blueprint, request, url_for)

from groundhog.sqreen_signature_verification import SqreenSignatureVerification
from groundhog.sqreen_report_dispatcher import SqreenReportDispatcher
from groundhog.logger import Logger

bp = Blueprint('sqreen_webhook_handler', __name__)

@bp.route('/receive_sqreen_alert', methods=['POST'])
def receive_sqreen_alert():

  SqreenWebhookHandler(request).run()

  return 'ok'


class SqreenWebhookHandler:

  NON_VERIFIED_MESSAGE_ALERT = "suspicious alert pretending to be Sqreen detected"

  def __init__(self, request):
    self.json_request = request.json
    self.bytestring_request = request.get_data()
    self.request_signature = request.headers['X-Sqreen-Integrity']

  def run(self):
    
    if SqreenSignatureVerification(self.request_signature, self.bytestring_request).run():
      SqreenReportDispatcher(self.json_request).run()
    else:
      Logger(self.NON_VERIFIED_MESSAGE_ALERT).run()