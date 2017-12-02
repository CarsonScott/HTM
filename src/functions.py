def sort(values):
	indices = [i for i in range(len(values))]
	done = False
	while not done:
		done = True
		for i in range(len(values)-1):
			if values[i] < values[i+1]:
				done = False
				value = values[i]
				index = indices[i]

				values[i] = values[i+1]
				indices[i] = indices[i+1]

				values[i+1] = value
				indices[i+1] = index
	return indices
