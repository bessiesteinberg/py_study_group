def list_user_permissions(user_id):
	# mocking accessing an actual data base
	permissions = {
		1: ['admin', 'logged_in'],
		2: ['logged_in']
		3: []
	}
	return permissions[user_id]


def requires_admin(some_function):
	def wrapper():
		permissions = list_user_permissions


class User(object):
	def __init__(self, id):
		self.id = id

	def get_admin_page(self):
		print "LOOK! An Admin page! SO much POWER!"

	def get_normal_page(self):
		print "Any logged in user can see this page, it's still pretty neat."


user_1 = User(1)
user_2 = User(2)
user_3 = User(3)

print("\nUser 1 has admin privledges:")
user_1.get_admin_page()
user_1.get_normal_page()

print("\nUser 2 is logged in, but not an admin:")
user_2.get_admin_page()
user_2.get_normal_page()

print("\nUser 3 exists, but is not logged in")
user_3.get_admin_page()
user_3.get_normal_page()
