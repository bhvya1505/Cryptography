from padding import padding
from Crypto.Cipher import AES
from Crypto import Random
from os import urandom

key = urandom(16)
print "Key: ", key.encode("hex")

cipher = AES.new(key, AES.MODE_ECB)
message = raw_input("Enter message ")
message = padding(message)
ciphertext = cipher.encrypt(message)
print ciphertext
print len(ciphertext)
print ciphertext.encode("hex")