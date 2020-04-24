plaintext = raw_input("Enter plaintext ")
ciphertext = ""
key = raw_input("Enter key ")

for i in range(len(plaintext)):
	k = i%len(key)
	ciphertext += chr(ord(plaintext[i])^ord(key[k]))
print ciphertext.encode("hex")
