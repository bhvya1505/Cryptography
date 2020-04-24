def padding(message):
	block_size = 16
	message_size = len(message)
	padding = block_size-message_size%block_size
	message += padding * chr(padding)
	return message

# message = raw_input("Enter message")
# print padding(message)