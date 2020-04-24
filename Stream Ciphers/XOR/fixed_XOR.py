import binascii
import base64

def decode_hex(ct):
	ct = binascii.unhexlify(ct)
	print(ct)
	return ct

def XOR(str1,str2):
	result = "".join(chr(i^j)) for i,j in zip(str1,str2)
	print result

string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"

string1 = decode_hex(string1)
XOR(string1,string2)

