def encrypted(string,shift):
	cypher=' '
	for char in string:
		if char==' ':
			cypher=cypher+char
		elif char.isupper():
			cypher=cypher+chr((ord(char)+shift-65)%26+65) #extract the ord of the character
								     #ASCII value of uppercase is 65
		else:
			cypher=cypher+chr((ord(char)+shift-97)%26+97)
	return cypher

def decrypt(string,shift):
	decypher=' '
	for char in string:
		if char==' ':
			decypher=decypher+char
		elif char.isupper():
			decypher=decypher+chr((ord(char)-shift-65)%26+65)
		else:
			decypher=decypher+chr((ord(char)-shift-97)%26+97)
	return decypher

menu=input("Choose(1.Encrypt/2.Decrypt): ")
if menu =="1":
	text=input("enter the text: ")
	shift=int(input("enter the shift key: "))
	print("the encrypted text is:",encrypted(text,shift))
elif menu =="2":
	text=input("enter the text: ")
	shift=int(input("enter the shift key: "))
	print("the encrypted text is:",decrypt(text,shift))
else:
	print("Choice is invalid. Exiting")
	exit()
	
	
# A basic and simple encryption and decryption of caesar cypher
#Reference: https://www.youtube.com/watch?v=Ws5E2gCW4Hc&t=601s&ab_channel=Iknowpython
