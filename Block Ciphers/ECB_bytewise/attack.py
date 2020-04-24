from pwn import *
r = process("./server.sh")

def block_length():
	i=1
	r.sendline("a")
	ct1 = r.recvline()[69:].strip()

	while True:
		r.sendline("a"*i)
		i+=1
		ct2 = r.recvline()[69:].strip()
		if len(ct1) == len(ct2):
			continue
		else:
			block_length = len(ct2.decode("hex")) - len(ct1.decode("hex"))
			break
		ct1 = ct2
	return block_length

def mode():
	size = block_length()
	r.sendline("a"*(size*2))
	ct = r.recvline()[69:].strip().decode("hex")
	if ct[:size] == ct[size:size*2]:
		return "ECB"
	else:
		return "not ECB"

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

print "Block length: ", block_length()
print "Mode: ", mode()
print "Secret: ", attack()