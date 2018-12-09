from sqreen_reports_formatter import SqreenReportsFormatter
from logger import Logger
from slacker import Slacker

class SqreenReportDispatcher:

  LIST_OF_MESSENGERS = [Logger, Slacker]

  def __init__(self, reports):
    self.message = SqreenReportsFormatter(reports).run()

  def run(self):
    self.send_message()    

  def send_message(self):
    for messenger in self.LIST_OF_MESSENGERS:
      messenger(self.message).run() 
