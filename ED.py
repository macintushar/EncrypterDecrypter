import getpass as gpass
import json
import os

#Functions
def encrypt(txt,file):
    x = []
    for i in txt:
        g = ord(i)
        x.append(g)
    print(x)
    with open (file,'w') as filehandle:
        json.dump(x,filehandle)

def decrypt(filename):
    with open(filename,'r') as filehandle:
        txt = json.load(filehandle)
    a = []
    for i in txt:
        y = chr(i)
        a.append(y)
    z = ''
    for i in a:
        z += i
    print(z)
    os.remove(filename)


pwd = 'User'
password = gpass.getpass()

if password == pwd:
    print("Options:")
    print("'encrypt' a message")
    print("'decrypt' a message")
    print("'exit'")
    while True:
        opt = input()
        if opt == 'encrypt':
            txt = input('Enter the message to encrypt: ')
            fname = input('Enter the File Name: ')
            fname += '.json'
            encrypt(txt,file=fname)
        
        if opt == 'decrypt':
            fname = input('Enter the File Name: ')
            fname += '.json'
            decrypt(filename=fname)

        if opt == 'exit':
            break

else:
    print("Stop trying to Unsuccessfully hack my Program and go get a life :)")
