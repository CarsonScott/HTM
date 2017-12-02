from functions import sort

class SpatialPooler:

	def __init__(self, nodes, inputs, learning_rate=0.001, pool_size=0.02, threshold=0.5):
		self.inputs = []
		self.outputs = []
		self.totals = []
		self.nodes = []
		self.links = []
		self.weights = []
		self.threshold = threshold
		self.psize = pool_size
		self.lrate = learning_rate
		for i in range(nodes):
			self.nodes.append(0)
			self.totals.append(0)
			self.outputs.append(0)
			self.weights.append([])
			self.links.append([])
		for i in range(inputs):
			self.inputs.append(0)

	def compute_totals(self):
		for i in range(len(self.nodes)):
			total = 0
			for j in range(len(self.links[i])):
				x = self.links[i][j]
				if self.weights[i][j] >= self.threshold:
					total += self.inputs[x]
			self.totals[i] = total

	def compute_outputs(self):
		for i in range(len(self.nodes)):
			output = self.totals[i]
			self.outputs[i] = output
		outputs = sort(self.outputs)
		size = int(len(outputs)*self.psize)
		for i in range(len(outputs)):
			n = outputs[i]
			if i < size:self.outputs[n] = 1
			else:self.outputs[n] = 0

	def compute_deltas(self):
		for i in range(len(self.nodes)):
			if self.outputs[i] == 1:
				for j in range(len(self.links[i])):
					if self.inputs[self.links[i][j]] == 1:
						self.weights[i][j] += self.lrate
					else:self.weights[i][j] -= self.lrate
					if self.weights[i][j] > 1:
						self.weights[i][j] = 1
					if self.weights[i][j] < 0:
						self.weights[i][j] = 0

	def update(self, x):
		self.inputs = x
		self.compute_totals()
		self.compute_outputs()
		self.compute_deltas()
		return self.outputs

