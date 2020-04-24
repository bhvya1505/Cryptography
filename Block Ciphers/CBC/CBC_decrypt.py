from Crypto.Cipher import AES

def validate(plaintext):
	n = ord(plaintext[-1])
	if n not in range(17):
		return False
	if plaintext[-n:]==n*chr(n):
		return True
	return False

def decrypt(ciphertext, key, iv):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	plaintext = cipher.decrypt(ciphertext)
	if validate(plaintext):
		return plaintext[:-ord(plaintext[-1])]

ciphertext = raw_input("Enter ciphertext ")
ciphertext = ciphertext.decode("hex")
key = raw_input("Enter key ")
key = key.decode("hex")
iv = raw_input("Enter iv ")
iv = iv.decode("hex")
print decrypt(ciphertext, key, iv)