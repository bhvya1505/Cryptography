from padding import padding
from Crypto.Cipher import AES
from os import urandom	

def XOR(str1,str2):
	pt = ""
	for i in range(len(str1)):
		pt += chr(ord(str1[i])^ord(str2[i]))
	return pt

key = urandom(16)
iv = urandom(16)
print key.encode("hex")
print iv.encode("hex")

message = raw_input("Enter message ")
message = padding(message)
plaintext = []

for i in range(0,len(message),16):
	plaintext.append(message[i:i+16])
print plaintext

ciphertext = []
IV = iv	
for i in range(len(plaintext)):
	pt = XOR(iv,plaintext[i])
	cipher = AES.new(key, AES.MODE_ECB)
	ciphertext.append(cipher.encrypt(pt))
	iv = ciphertext[i]
print IV.encode("hex") + "".join(ciphertext).encode("hex")



