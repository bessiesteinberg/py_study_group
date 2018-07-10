class Accumulator(list):
	pass

sad_code_base = Accumulator()
sad_code_base.append("tech_debt")
sad_code_base.append("cruft")
sad_code_base.append("no really this is a good idea")
print sad_code_base[:]

sad_code_base.pop()
print sad_code_base[:]

other_code_base = sad_code_base + [ 1 ]
print(type(other_code_base))