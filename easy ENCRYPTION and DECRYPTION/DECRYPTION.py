import time

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',' ']


def split(word):
	return [char for char in word]

def delay(seconds):
	time.sleep(seconds)

def decrypt_string(inputString):
	OUTPUTSTRING = ""
	for posibilities in range(len(alphabet)):
		for letters in range(len(inputString)):
			for findChar in range(len(alphabet)):
				if inputString[letters] == alphabet[findChar]:
					try:
						OUTPUTSTRING += str(alphabet[findChar + posibilities])
					except:
						OUTPUTSTRING += str(alphabet[findChar + posibilities - len(alphabet)])

		print("#" + str(posibilities+1) + " = ", end = "")
		print(OUTPUTSTRING)
		OUTPUTSTRING =""

while True:
	print("Inut encrypted string: ", end = "")
	inputString = input()
	inputString = split(inputString)
	decrypt_string(inputString)
	print("DONE")
	print("")
	print("WHICH ONE IS RIGHT: ", end ="")
	ENCRYPTIONNUMBER = input()
	ENCRYPTIONNUMBER = int(ENCRYPTIONNUMBER)
	ENCRYPTIONNUMBER = 38 - ENCRYPTIONNUMBER
	print("Encrypion key = " + str(ENCRYPTIONNUMBER) , end = "\n\n")
	delay(1)



