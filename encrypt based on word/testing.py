
def get_values_list(input_string):
	OUTPUTLIST = list()
	for letter in input_string:
		OUTPUTLIST.append(ord(letter))
	return OUTPUTLIST

def get_message_from_values(values_list):
	OUTPUT_MESSAGE = ""
	for letter in values_list:
		OUTPUT_MESSAGE += chr(letter)
	return OUTPUT_MESSAGE 

def encrypt_message(message,key):
	ENCRYPTED_MESSAGE = ""

	message_values = get_values_list(message)
	key_values = get_values_list(key)

	MESSAGE_ENCRYPTED_VALUES_LIST = list()

	key_list_index = 0
	for character in range(len(message_values)):
		MESSAGE_ENCRYPTED_VALUES_LIST.append(message_values[character] + key_values[key_list_index])
		if key_list_index == len(key_values) - 1:
			key_list_index = 0
		else:
			key_list_index += 1 

	ENCRYPTED_MESSAGE = get_message_from_values(MESSAGE_ENCRYPTED_VALUES_LIST)
	return ENCRYPTED_MESSAGE

def decrypt_message(message,key):
	DECRYPTED_MESSAGE = ""

	message_values = get_values_list(message)
	key_values = get_values_list(key)

	MESSAGE_DECRYPTED_VALUES_LIST = list()

	key_list_index = 0
	for character in range(len(message_values)):
		MESSAGE_DECRYPTED_VALUES_LIST.append(message_values[character] - key_values[key_list_index])
		if key_list_index == len(key_values) - 1:
			key_list_index = 0
		else:
			key_list_index += 1 

	DECRYPTED_MESSAGE = get_message_from_values(MESSAGE_DECRYPTED_VALUES_LIST)
	return DECRYPTED_MESSAGE

message = "this is a secret message"
key = "thisisasecretkey"

encrypted = encrypt_message(message,key)
print(encrypted)
decrypted = decrypt_message(encrypted,key)
print(decrypted)