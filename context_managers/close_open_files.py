for x in range(10000):
	file_name = "foo{}.txt".format(x)
	file = open(file_name,'w')
	file.close()
