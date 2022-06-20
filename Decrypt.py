#!/usr/bin/env python3
import StreamCP
import getpass
import time
import os
PASS = 'time.pass'
NAME = 'crypt'
def main():
    filename = input("请输入待解密的文件\n:")
    filename2 = NAME
    pawd = getpass.getpass('请输入密码\n:')
    path = filename
    nonce = ''
    with open(filename+'/'+PASS) as f:
        nonce=f.read()
        f.close()
    
    pd = list(pawd)
    key1 = []
    key2 = []
    for y in pd:
        key1.append(ord(y))#密码字节化
    
    for y in nonce:
        key2.append(ord(y))#时间戳字节化
    
    StreamCP.crypto(filename, filename2, key1, key2, PD=False)
    
        
if __name__ == "__main__":
    main()