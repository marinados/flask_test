from groundhog.sqreen_alert_message import SqreenAlertMessage

class SqreenReportDispatcher:

  def __init__(self, reports):
    self.message = SqreenAlertMessage(reports)

  def run(self):
    self.send_message()    

  def send_message(self):
    for messenger in self.message.target_backends:
      messenger(self.message.text).run() 
