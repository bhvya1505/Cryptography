from Crypto.Cipher import AES

def XOR(str1,str2):
	pt = ""
	for i in range(len(str1)):
		pt += chr(ord(str1[i])^ord(str2[i]))
	return pt

def validate(plaintext):
	n = ord(plaintext[-1])
	if n not in range(17):
		return False
	if plaintext[-n:]==n*chr(n):
		return True
	return False

ciphertext = raw_input("Enter ciphertext ")
ciphertext = ciphertext.decode("hex")
key = raw_input("Enter key ")
key = key.decode("hex")

ct = []
iv = ciphertext[:16]
for i in range(16, len(ciphertext), 16):
	ct.append(ciphertext[i:i+16])
print ct

plaintext = []
for i in range(len(ct)):
	cipher = AES.new(key, AES.MODE_ECB)
	temp = cipher.decrypt(ct[i])
	plaintext.append(XOR(iv,temp))
	iv = ct[i]
message = "".join(plaintext)

if validate(message):
	print message[:ord(message[-1])]