from Crypto.Cipher import AES

def validate(plaintext):
	n = ord(plaintext[-1])
	if n not in range(17):
		return False
	if plaintext[-n:]==n*chr(n):
		return True
	return False

def decryption(ciphertext, key):
	cipher = AES.new(key, AES.MODE_ECB)
	plaintext = cipher.decrypt(ciphertext)
	if validate(plaintext):
		return plaintext[:-ord(plaintext[-1])]

ciphertext = raw_input("Enter ciphertext ")
ciphertext = ciphertext.decode("hex")
key = raw_input("Enter key ")
key = key.decode("hex")
print decryption(ciphertext, key)