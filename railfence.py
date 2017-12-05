class Railfence:
        def __init__(self,key,text):
                self.ciphername = "Railfence"
                self.key = int(key)
                self.text = list(text)
                # 10/3 +10mod3
                #print len(self.text)/self.key+len(self.text)%self.key
                self.columns = int(len(self.text)/self.key + 1)
                self.table = []

        def prep_table(self):
                for row in range(self.key):
                        self.table.append([])
                        for column in range(self.columns):
                                self.table[row].append(" ")
				
        def encrypt(self):
                count = 0
                self.prep_table()
                for column in range(self.columns):
                        for row in range(self.key):
                                if count>len(self.text)-1:
                                        self.table[row][column]=" "
                                else:
                                        self.table[row][column] = self.text[count]
                                count+=1
                #print("columns = ",self.columns)
                #print(len(self.text)/self.key)
                #print(len(self.text)%self.key)
                ciphertext = ""
                for row in self.table:
                        for element in row:
                                if element != ' ':
                                        ciphertext += element

                if self.table[0][-1] == " ":
                        for i in range(len(self.table)):
                                del self.table[i][-1]
                for i in self.table:
                        print(i)
                print(ciphertext)
                return ciphertext

        def decrypt(self):
                whitespace = self.columns*self.key - len(self.text)
                if whitespace > self.key:
                        whitespace -= self.key
                        self.columns -= 1

                for i in range(self.columns, len(self.text), self.columns):
                        if whitespace != 0:
                                self.text.insert(i * 2 - 1, " ")

                for i in range(self.key):
                        self.table.append(self.text[i * self.columns:i*self.columns*self.columns])
                print(self.text)
                print(whitespace)
                for i in self.table:
                        print(i)

                plaintext = " "
                for column in range(self.columns):
                        for row in range(self.key):
                                if self.table[row][column] != " ":
                                        plaintext += self.table[row][column]
                print("Decrypting with" + self.ciphername)
                print(plaintext)
                return plaintext

#Railfence(5, "muroikartudeyhbriyyeegnoayug").decrypt()
#Railfence(3, "meetmeatthetogaparty").encrypt()
