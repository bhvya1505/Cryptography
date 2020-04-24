ciphertext = "bqnrrhmfsgdqtahbnmxjvkipdb"
#plaintext = ""
small = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(n):
	plaintext = ""
	for j in ciphertext:
		if j in small:
			plaintext += small[(small.index(j)-n)%26]
		elif j in capital:
			plaintext += capital[(capital.index(j)-n)%26]
		else:
			plaintext += j
	print n,plaintext
for i in range(26):
	decrypt(i)

