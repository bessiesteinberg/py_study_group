class Server:

	services = [
  		{'active': True, 'protocal': 'http', 'port': 12},
  		{'active': False, 'protocal': 'ftp', 'port': 34},
  		{'active': True, 'protocal': 'ssh', 'port': 56},
  		{'active': False, 'protocal': 'tcp', 'port': 78},
  		{'active': True, 'protocal': 'ssh', 'port': 90},
	]

	def __iter__(self):
		for service in self.services:
			if service['active']:
				yield service

my_server = Server()
for service in my_server:
	print(service)