class Vigenre:
	def __init__(self,key,text):
		self.ciphername = "Vigenre"
		self.key = key
		self.text = text
		self.length = len(self.text)
		self.table = []
		self.set_table()

	def encrypt(self):
		print "Encrypting with "+self.ciphername
		plaintext = ""
		for i in range(self.length):
			plaintext+=self.table[i+1][self.table[0].index(self.text[i])]
		print plaintext
		return plaintext

	def decrypt(self):
		print "Decrypting with "+self.ciphername
		ciphertext = ""
		for i in range(self.length):
			position = self.table[i+1].index(self.text[i])
			ciphertext += self.table[0][position]
		print ciphertext
		return ciphertext

	def set_table(self):
		alphabet = list("abcdefghijklmnopqrstuvwxyz")
		self.table.append(alphabet)
		for letter in self.prep_key():
			pos =  alphabet.index(letter)
			self.table.append(alphabet[pos:]+alphabet[:pos])
			
	def prep_key(self):
		count = 0
		prep_key = ""
		for i in range(len(self.text)):
			prep_key +=self.key[count]
			if count==len(self.key)-1:
				count=0
			else:
				count+=1
		return prep_key