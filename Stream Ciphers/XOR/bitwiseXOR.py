plaintext = raw_input("Enter plaintext ")
key = input("Enter key ")
ciphertext = ""
for i in plaintext:
	ciphertext += chr(ord(i)^key)
print ciphertext