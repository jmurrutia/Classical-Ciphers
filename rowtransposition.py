import math

class rowtransposition():
    'Row Transposition Cipher'
	
    def __init__(self, key, text, to_encrypt):
        self.key = str(key)
        self.text = list(text)
        self.textLength = len(self.text)
        self.keyLength = len(self.key)
        self.rowNum = math.ceil(self.textLength / self.keyLength)
        self.table = []
        self.to_encrypt = to_encrypt
        self.set_table()
        self.newKey = self.generatenewKey()
        if self.to_encrypt:
            self.encrypt()
        else:
            self.decrypt()

    # This function will create an empty matrix of appropriate size
    def set_table(self):
        for row in range(self.rowNum):
            self.table.append([])
            for column in range(self.keyLength):
                self.table[row].append(' ')

    # This function will create a list name 'newKeky' for the purposes of printing the ciphertext
    # in the correct order, as well as placing the ciphertext in correct order to print the plaintext
    def generatenewKey(self):
        newKey = []
        for i in range(self.keyLength):
            newKey.append(int(self.key[i]))
        return newKey

    # Encrypt function 
    def encrypt(self):
        row = 0
        count = 0
        spaces = 0
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        ciphertext = ""

        # For loop used to fill in the matrix with plaintext
        for row in range(self.rowNum):
            for column in range(self.keyLength):
                # This if statement keeps track of the number of junk letters that will need to be
                # inputted into the plaintext text for encryption
                if count >= self.textLength:
                    self.table[row][column] = " "
                    spaces += 1
                else:
                    self.table[row][column] = self.text[count]
                    count += 1
            #  This if statement inserts the junk letters in the plaintext
            if spaces > 0:
                for row in range(self.rowNum):
                    for column in range(self.keyLength):
                        if self.table[row][column] == ' ':
                            self.table[row][column] = alphabet[len(alphabet) - spaces]
                            spaces -= 1
        
        print("We are going to encrypt the plaintext " + ''.join(self.text), end=' ' + "with key " + str(self.key))
        print("\n")
        #for i in self.table:
        #    print(i)

        #  For loop to place characters of the plaintext in the order provided by the key, to create ciphertext
        for i in range(len(self.newKey)):
            col = self.newKey[i] - 1
            for row in range(self.rowNum):
                ciphertext += self.table[row][col]

        print("\nThe ciphertext is", ciphertext)
	
    def decrypt(self):
        row = 0
        count = 0
        plaintext = ""

        #  This for loop will place the cipertext in the correct order according to the key provided
        for i in range(len(self.newKey)):
            column = self.newKey[i] - 1
            for row in range(self.rowNum):
                self.table[row][column] = self.text[count]
                count += 1

        print("We are going to decrypt the ciphertext " + ''.join(self.text), end=' ' + "with key " + str(self.key))
        print("\n")
        #for i in self.table:
        #    print(i)

        #  This for loop will create the plaintext in the order provided by the key
        for row in range(self.rowNum):
            for column in range(self.keyLength):
                plaintext += self.table[row][column]
            

        print("\nThe plaintext is", plaintext)
            

#rowtransposition(3421567, 'attackpostponeduntiltwoam', True)
#rowtransposition(3421567, 'ttnaaptmtsuoaodwcoixknlypetz', False)
