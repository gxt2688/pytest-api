from hashlib import sha1
from hashlib import md5
from crpto.Hash import SHA256
from crpto.Cipher import AES
from crpto.Cipher import DES
import binascii


def my_md5(msg):
    '''
       md5 算法加密
       :param msg:需加密字符串
       :return:加密后的字符
       '''
    h1=md5()
    h1.update(msg.encode('utf-8'))
    return h1.hexdigest()
   
def my_sha1(msg):
    sh = sha1()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()
def my_sha256(msg):
    sh = SHA256.new()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()
def my_aes(msg):
    sh = AES.new()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()
def my_des(msg,key):
    de = DES.new(key, DES.MODE_ECB)
    mss=msg+(8-(len(msg)%8))*'='
    text=de.encrypt(mss.encode())
    return binascii.b2a_hex(text).decode()
def my_aes_encrypt(msg,key,vi):
    '''
      AES算法解密
      :param msg:需解密的字符串
      :param key:必须为16，24，32位
      :param vi:必须为16位
      :return：加密后的字符
      '''
    obj=AES.new(key,AES.MODE_CBC,vi)
    return obj.decrypt(msg).decode()

