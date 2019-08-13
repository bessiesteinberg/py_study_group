class Accumulator(list):
	pass

hamilton = Accumulator()

hamilton.append("power")
hamilton.append("debt")
print("\nhamilton[:]: {}".format( hamilton[:] ))

print("\n\"ounce of regret\" in hamilton: {}".format(
	"ounce of regret" in hamilton
))

print()