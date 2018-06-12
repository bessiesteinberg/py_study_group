f=open("my_config.ini")
for line in f:
	line = line.strip()
	if line.startswith('#'):
		# A commend line, skip it. 
		continue
	if not line:
		# A blank line, skip it.
		continue

	# An interesting line
	do_something(line)

def interesting_lines(f):
	for line in f:
		line = line.strip()
		if line.startswith('#'):
			continue
		if not line:
			continue
		yield line

with open("my_config.ini") as f:
	for line in interesting_lines(f):
		do_something(line)

with open("my_other.dat") as f2:
	for line in interesting_lines(f2):
		do_something_else(line)