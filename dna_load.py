import numpy as np

class DnaLoad:

	def __init__(self, file_name): 
		self.input_file = file_name
		self.f = None
		self.sequence = None
		self.lab = None

		self.read_from_file()
		self.generate_sequence()


	def read_from_file(self):
		self.f = open(self.input_file, 'r').readlines()

	def generate_sequence(self):
		self.sequence = self.f[0].split(';')[1]
		self.lab = self.f[0].split(';')[3]

	def get_labels(self, fseq, window_size, stride):
		l = windows(fseq, window_size, stride)
		arr = np.zeros(len(l))
		for i in range(len(l)):
			ones = 0
			for j in range(len(l[i])):
				if l[i][j] == '1':
					ones+=1
			if ones>=2:
				arr[i] = 1
				
		return arr


	def windows(self, fseq, window_size, stride):
		list_of_k_mers = []
		for seq in window_samples(fseq, window_size, stride):
			list_of_k_mers.append(seq)
		return list_of_k_mers


	def window_samples(self, fseq, window_size, stride):
		if len(fseq)>2*window_size:
			for i in range(0, len(fseq) - window_size + 1, stride):
				yield fseq[i:i+window_size]

dna_load = DnaLoad("input_file.txt")

