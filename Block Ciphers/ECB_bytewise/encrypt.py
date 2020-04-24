from Crypto.Cipher import AES
#from os import urandom

secret = open("secret.txt").read().strip()
key = open("key.txt").read().strip().decode("hex")
block_size = int(open("block_size.txt").read().strip())

def padding(message, block_size):
	message_size = len(message)
	padding = block_size-message_size%block_size
	message += padding * chr(padding)
	return message

def encrypt(plaintext, key):
	plaintext += secret
	cipher = AES.new(key, AES.MODE_ECB)
	plaintext = padding(plaintext, block_size)
	ciphertext = cipher.encrypt(plaintext)
	return ciphertext.encode("hex")

while True:
	message = raw_input("Hello User! Give me a message to encrypt. ")
	print "Your encrypted message is " , encrypt(message, key)