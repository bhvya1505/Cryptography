import binascii
import base64

def decode_hex(ct):
	ct = binascii.unhexlify(ct)
	print(ct)
	return ct

def encode_base64(pt):
	pt = base64.b64encode(pt)
	print(pt)

ciphertext = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
plaintext = decode_hex(ciphertext)
encode_base64(plaintext)

#"I'm killing your brain like a poisonous mushroom"
#'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
