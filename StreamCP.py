#!/usr/bin/env python3
import tqdm
import os
import time
import re
import getpass
import struct, base64

SIZE = 512
def read_in_chunks(file_obj, chunks_size = SIZE):
    '''
    读取文件
    默认大小
    '''
    while True:
        data = file_obj.read(chunks_size)
        if not data:
            break
        yield data

def crypto(filename, filename2, key, nonce, PD=True):
    T = [] #辅助数组
    S = [] #生成256字节密钥
    for i in range(256):
        T.append(int(key[i%len(key)]&nonce[i%len(nonce)])) 
        S.append(i)
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i])%256
        S[i], S[j] = S[j], S[i]
    m, n = 0, 0
#    res = bytes()
    fsize = os.path.getsize(filename)
    tot = int(fsize)
    print("文件大小(Bytes): ")
    print(tot)
    pbar = tqdm.tqdm(total=tot)
    if PD==True :#加密
        with open(filename, 'rb') as f:
            for p1 in read_in_chunks(f): #取SIZE字节的文件
                res = bytes()
                for p in p1:#对每一字节处理
                    '''
                    S[i]密钥与明文异或
                    '''
                    m = (m+1)%256
                    n = (n+S[m])%256
                    S[m],S[n] = S[n], S[m]
                    t = (S[m]+S[j])%256
                    res +=bytes([p^S[t]])#按字节加密
                with open(filename+'_dir/'+filename2, 'ab') as f2:
                    f2.write(res)
                f2.close()
                pbar.update(SIZE)
        f.close()
        pbar.close()
    else : #解密
        with open(filename+'/'+filename2, 'rb') as f:
            for p1 in read_in_chunks(f): #取SIZE字节的文件
                res = bytes()
                for p in p1:#对每一字节处理
                    '''
                    S[i]密钥与明文异或
                    '''
                    m = (m+1)%256
                    n = (n+S[m])%256
                    S[m],S[n] = S[n], S[m]
                    t = (S[m]+S[j])%256
                    res +=bytes([p^S[t]])#按字节加密
                with open(filename+'.OUT', 'ab') as f2:
                    f2.write(res)
                f2.close()
                pbar.update(SIZE)
        f.close()
        pbar.close()
        
    return True

def main():
    print("注意二次加密就是解密")
    filename = input("请输入待加密的文件\n:")
    filename2 = input("请输入加密后的文件名\n:")
    # filename2 = filename.replace(".","-")+'.out'
    pawd = getpass.getpass('请输入密码\n:')
    pd = list(pawd)
    pdd = []
    for y in pd:
        pdd.append(ord(y))#密码字节化
    tot = 1 
    print("第{0}次迭代".format(tot))
    print("加密/解密文件:("+filename+') to>>>> '+filename2)
    crypto(filename, filename2, pdd)
    print("output:"+filename2)
    filename, filename2 = filename2, filename

if __name__ == "__main__":
    main()
    print("end")
