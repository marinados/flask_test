class SqreenReportFormatter:
  # sample
  # [{'application_name': 'crabshelter', 'event_category': 'http_error', 'event_kind': 'bot_scanning', 
  # 'url': 
  # 'https://my.sqreen.io/application/6cf7ade4d1854e5baf4c18adbd08e8e0accb47e93a7c4c648cd6049c9f31109c/events/5c0d328794a2e000081f9234', 
  # 'environment': 'development', 
  # 'ips': [{'hostname': 'static-5-51-199-63.ftth.abo.bbox.fr', 
  # 'geo': {'code': 'FRA', 'city': 'Paris', 'point': [2.3003, 48.8412]}, 
  # 'address': '5.51.199.63', 
  # 'is_tor': False, 'date_resolved': '2018-12-09T15:19:35.931000+00:00'}], 
  # 'date_occurred': '2018-12-09T15:19:35.746000+00:00', 
  # 'humanized_description': 'Potential Automated Vulnerability discovery from 5.51.199.63', 
  # 'risk': 50, 'id': '5c0d328794a2e000081f9234', 
  # 'application_id': '5c029947a3e2f9001df7006f', 
  # 'sqreen_payload_type': 'security_event'}]
	def run(report):
    