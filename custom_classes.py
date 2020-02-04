class rcell_modem_object(object):
	def __init__(self, store_modem_data, url, successfull_request1, successfull_request2, successfull_request3, successfull_request4):
		self.store_modem_data = store_modem_data
		self.url = url
		self.successfull_request1 = successfull_request1
		self.successfull_request2 = successfull_request2
		self.successfull_request3 = successfull_request3
		self.successfull_request4 = successfull_request4


class sierra_modem_object(object):
	def __init__(self, store_modem_data, url, successfull_request1, successfull_request2, successfull_request3):
		self.store_modem_data = store_modem_data
		self.url = url
		self.successfull_request1 = successfull_request1
		self.successfull_request2 = successfull_request2
		self.successfull_request3 = successfull_request3
