#!/usr/bin/env python3
import StreamCP
import getpass
import time
import os
PASS = 'time.pass'
NAME = 'crypt'

def main():
    filename = input("请输入待加密的文件\n:")
    filename2 = NAME
    pawd = getpass.getpass('请输入密码\n:')
    path = filename+'_dir'
    
    # 创建文件夹
    if not os.path.exists(path):
        os.mkdir(path)
        time.sleep(0.5)
        print("创建成功！")
    else:
        print("文件夹存在")
    
    pd = list(pawd)
    millis = int(round(time.time() * 1000))
    millis = hex(millis)
    with open(path+'/'+PASS, 'w') as fh:
        fh.write(millis)
    fh.close()
    
    # open(filename+'/'+NAME, 'w')
    key1 = []
    key2 = []
    for y in pd:
        key1.append(ord(y))#密码字节化
    
    for y in millis:
        key2.append(ord(y))#时间戳字节化
    
    StreamCP.crypto(filename, filename2, key1, key2, PD=True)
    
        
if __name__ == "__main__":
    main()