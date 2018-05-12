import socket

def Main():
	host = '127.0.0.1'
	port = input("enter a client port")

	server = ('127.0.0.1', 6000)

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	message = raw_input("=> ")
	while message != 'quit':
		s.sendto(message, server)
		data, addr = s.recvfrom(1024)
		print "received from server" + str(data)
		message = raw_input("=> ")
	s.close()

if __name__ == '__main__':
	Main()
