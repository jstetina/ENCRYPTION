#ENCRYPT DECRYPT
import time

ENCRYPTIONkey = 17
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',' ']
def split(word):
	return [char for char in word]

def delay(seconds):
	time.sleep(seconds)

def encryptString(inputString):
	ENCRYPTEDSTRING = ""
	for letter in range(len(word)):
		for findChar in range(len(alphabet)):
			if word[letter] == alphabet[findChar]:
				if findChar + ENCRYPTIONkey > len(alphabet) - 1:
					ENCRYPTEDSTRING += str(alphabet[findChar - len(alphabet) + ENCRYPTIONkey])
				else:
					ENCRYPTEDSTRING += str(alphabet[findChar+ENCRYPTIONkey])

	return ENCRYPTEDSTRING

	
while True:
	print("Input unecrypted string: ", end = "")
	word = input()
	word = split(word)

	print("ENCRYPTED: ", end = "")
	print(encryptString(word), end = "\n\n")

	delay(1)

input("press any key to EXIT")
sys.exit()





