from Crypto.Cipher import AES

str1 = open("str1.txt").read().strip()
str2 = open("str2.txt").read().strip()
IV = open("iv.txt").read().strip().decode("hex")
key = open("key.txt").read().strip().decode("hex")	
block_size = int(open("block_size.txt").read().strip())

def padding(message, block_size):
	message_size = len(message)
	padding = block_size-message_size%block_size
	message += padding * chr(padding)
	return message

def encrypt(plaintext):
	plaintext = plaintext.replace(" ","?")
	plaintext = plaintext.replace("_","?")
	print plaintext
	message = str1+plaintext+str2
	cipher = AES.new(key, AES.MODE_CBC, IV)
	message = padding(message, block_size)
	ciphertext = cipher.encrypt(message)
	return ciphertext.encode("hex")



while True:
	payload = raw_input("Hello user, give me your payload: ")
	print "Your encrypted message is ", encrypt(payload)
