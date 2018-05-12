import socket

def Main():
	host = '127.0.0.1'
	port = 6000

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	print "UDP server started"
	while True:
		data, addr = s.recvfrom(1024)
		print "message from " + str(addr)
		print "from connect user: " + str(data)
		data = str(data).upper()
		print "ACKING " + str(data)
		s.sendto(data, addr)
	s.close()

if __name__ == '__main__':
	Main()
