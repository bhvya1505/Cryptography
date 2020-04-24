from pwn import *
r = process("./server.sh")

def attack():
	secret = ""
	r.sendline("a"*15)
	ciphertext =r.recvline()[69:].replace("\n", "").decode("hex")
	print len(ciphertext)
		
	for k in range(len(ciphertext)/16):
		size = 16*(k+1)
		size1 = 16*k
		for i in range(15,-1,-1):
			r.sendline("a"*i)
			ct1 = (r.recvline()[69:].replace("\n", "").decode("hex"))[size1:size]
			
			temp = "a"*i + secret
			for j in range(256):
				if j==10:
					continue
				else:
					r.sendline(temp+chr(j))
					ct2 = (r.recvline()[69:].replace("\n", "").decode("hex"))[size1:size]
					if ct1 == ct2:
						secret += chr(j)
						break
	print secret
	print len(secret)


attack()