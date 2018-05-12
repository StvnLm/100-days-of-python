import socket

def Main():
	host = '127.0.0.1'
	port = input("enter port")

	s = socket.socket()
	s.connect((host, port))

	message = raw_input("-> ")
	while message != 'quit':
		s.send(message)
		data = s.recv(1024)
		print "recieved from server " + str(data)
		message = raw_input("-> ")
	s.close()

if __name__ == '__main__':
	Main()
