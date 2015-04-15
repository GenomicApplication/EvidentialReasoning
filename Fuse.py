
massA = {('ad', 'ae', 'af'): 0.2, ('cd', 'ce', 'cf'): 0.3, 'theta': 0.5}

massB = {('ad', 'bd', 'cd', 'ae', 'be', 'ce'): 0.4, ('af', 'bf', 'cf'): 0.3, 'theta': 0.3}

def fuse(massA, massB):
	i = 0
	for keys in massA:
		a = 0
		print (keys, massB.keys()[a])
		if keys == "theta" or massB.keys()[a] == 'theta':
			result = massA.values()[i] * massB.values()[a]
			print (result)

		elif any(keys in massB.keys()[a] for keys in massB.keys()):
			result1 = massA.values()[i] * massB.values()[a]
			print (result1)

		elif any(keys not in massB.keys()[a] for keys in massB.keys()):
			k = massA.values()[i] * massB.values()[a]
			result2 = 1/(1-k)
			print (result2)
	i = i + 1
	a = a + 1





fuse(massA, massB)

