# -*- coding: utf-8 -*-
import socket
import sys

#-----------------------------
'''Handle the CTRL-C signal.'''
def close_socket(sig):
    print('Socket Closed')
    s.send('quit'.encode()) #inform server of closing  
    s.close()
    sys.exit(1)

# def install_handler():
    # if 'win' in sys.platform :
        # import win32api
        # win32api.SetConsoleCtrlHandler(close_socket, True)
    # elif 'linux' in sys.platform :
        # print('you may install crtl-C signal handler for Linux')        

# install_handler()
#--------------------------------------------

TARGET_HOST = '127.0.0.1' #要連接的IP
#HOST = '125.229.69.35'
TARGET_PORT = 7000 #要連接的port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #建立TCP/IP
s.connect((TARGET_HOST, TARGET_PORT))#連線到要連接的IP/PORT

while True:
    outdata = input('please input message: ')

    print('send: ' + outdata)
    s.send(outdata.encode())
    if outdata=='quit':
        break

    
s.close()
print('Client closed connection.')