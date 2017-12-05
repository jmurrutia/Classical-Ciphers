import sys
import playfair
import railfence
import caesar
import row_transposition
import vigenre

class CipherInterface:
	def __init__(self,cipher,key,to_encrypt,text):
		self.to_encrypt = to_encrypt
		if cipher == "PLF":
			self.cipher = playfair.Playfair(key,text)
			
		elif cipher == "RTS":
			self.cipher = row_transposition.Row_Transposition(key,text)
			
		elif cipher == "VIG":
			self.cipher = vigenre.Vigenre(key,text)
		elif cipher == "RFC":
			self.cipher = railfence.Railfence(key,text)
			
		elif cipher == "CES":
			self.cipher = caesar.Caesar(key,text)
		else:
			print("Cipher not recognized.")

	def output(self):
		if self.to_encrypt == "ENC":
			return self.cipher.encrypt()
		elif self.to_encrypt == "DEC":
			return self.cipher.decrypt()
		else:
			return "Encrypt or Decrypt?"


args = sys.argv
if args[1]== "help":
	print()
	print("Format")
	print("======")
	print("python cipher.py <cipher> <key> <ENC/DEC> <inputfile> <outputfile>")
	print()
	print("Ciphers")
	print("======")
	print("Playfair = PLF")
	print("Row Transposition = RTS")
	print("Vigenre = VIG")
	print("Railfence = RFC")
	print("Caesar = CES")
elif len(args)==6:
	cipher = args[1]
	key = str(args[2])
	to_encrypt = args[3]
	inputf = args[4]
	outputf = args[5]
	inputfile = open(inputf, 'r')
	text = inputfile.readline()

	cipherinput = CipherInterface(cipher,key,to_encrypt,text)
	outputfile = open(outputf, 'w')

	outputfile.write(cipherinput.output())
	inputfile.close()
	outputfile.close()
else:
	print("Invalid input. Type \"python cipher.py help\"")
