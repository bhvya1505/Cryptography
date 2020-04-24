ciphertext = raw_input("Enter ciphertext ")

def decrypt(n):
	plaintext = ""
	for j in ciphertext:
		plaintext += chr(ord(j)^n)
	print plaintext

for i in range(256):
	decrypt(i)
