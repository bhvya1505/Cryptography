plaintext = raw_input("Enter your plaintext: ")
key = input("Enter the key: ")

ciphertext = ""
small = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in plaintext:
	if i in small:
		ciphertext += small[(small.index(i)+key)%26]
	elif i in capital:
		ciphertext += capital[(capital.index(i)+key)%26]
	else:
		ciphertext += i

print ciphertext

