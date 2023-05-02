# -*- coding: utf-8 -*-
"""
Created on Oct 29,2022
@author: joseph@艾思程式教育

Simple TCP server

"""
import socket
import sys

#-----------------------------
'''Handle the CTRL-C signal.'''
def close_socket(sig):
    print('Server Socket Closed')
    server_socket.close()
    sys.exit(1)

# def install_handler():
    # if 'win' in sys.platform :
        # import win32api
        # win32api.SetConsoleCtrlHandler(close_socket, True)
    # elif 'linux' in sys.platform :
        # print('you may install crtl-C signal handler for Linux')        

# install_handler()
#--------------------------------------------

HOST = '0.0.0.0' #任意IP皆可連接
PORT = 7000 #設定自己的port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #建立TCP/IP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #建立socket

server_socket.bind((HOST, PORT)) #任意IP可連接 自己的port為7000
server_socket.listen(5) #最多一次可以有五個客戶端連接

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    try:
        conn, addr = server_socket.accept()
        print("Connection from: " + str(addr))
    except socket.error as e: 
        print('Abnormally terminate program')
        sys.exit(1)

    while True:
        try :
            indata = conn.recv(1024) #接收客戶端傳輸過來的資料
        except socket.error as e: 
            #print("Client Connection error: %s" % e)    
            print("Client (%s, %s) is offline" % addr)                     
            break
            
        if len(indata) == 0 or indata.decode()=='quit': # connection closed
            conn.close()
            print("Client (%s, %s) is offline" % addr)
            break
        
        print('recv: ' + indata.decode())
          
        #echo the message to client
        outdata = 'echo ' + indata.decode()
        conn.send(outdata.encode())




