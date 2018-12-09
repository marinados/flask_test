from sqreen_report_formatter import SqreenReportFormatter
from emailer import Emailer
from slacker import Slacker


class SqreenReportDispatcher:

  LIST_OF_MESSANGERS = [Emailer, Slacker]
  
  def run(report):
    message = message_for(report)
    send_message(message)

  def message_for(report):
    SqreenReportFormatter.run(report)

  def send_message(message):
    for messanger in LIST_OF_MESSANGERS:
      messanger.run(message) 
