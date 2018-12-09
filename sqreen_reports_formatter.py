import datetime

class SqreenReportsFormatter:

  def __init__(self, reports):
    self.reports = reports

  def run(self):
    formatted_reports = list(map(lambda report: self.format(report), self.reports))
    return '; '.join(formatted_reports)

  def format(self, report):
    report_type = report['sqreen_payload_type']
    if report_type == 'security_event':
      return self.security_event_message(report)
    elif report_type == 'pulse':
      return self.pulse_message(report)
    elif report_type == 'security_response':
      return self.security_event_message(report)
    else:
      return self.unrecognized_message()

  @staticmethod
  def security_event_message(report):
    date = report['date_occurred']
    description = report['humanized_description']
    url = report['url']
    return f'The Sqreen security event alert received on {date}: {description}, for details visit {url}'
    
  @staticmethod
  def pulse_message(report):
    title = report['humanized_title']
    date = report['date_started']
    url = report['url']
    return f'The Sqreen pulse alert: {title} that started on {date}, for details visit {url}'
    
  @staticmethod
  def security_response_message(report):
    playbook = report['playbook']['name']
    date = report['date_created']
    return f'The Sqreen securiry response alert: {playbook} triggered on {date}'
    
  @staticmethod
  def unrecognized_message():
    f'The Sqreen webhook message received on {datetime.datetime.now()} has not been recognized'
