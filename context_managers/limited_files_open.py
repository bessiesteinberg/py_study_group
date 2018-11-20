# warning! doing this on a windows may crash your machine :[
files = []
for x in range(100000):
	file_name = "foo{}.txt".format(x)
	files.append(open(file_name,'w'))

