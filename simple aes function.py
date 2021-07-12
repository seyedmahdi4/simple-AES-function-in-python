#pip install cryptography

from cryptography.fernet import Fernet


key = Fernet.generate_key()
#print(key)  #for save it
#---or---
#key = ........


#----or this method for genrate key-----
#import base64,os
#base64.urlsafe_b64encode(os.urandom(32))
# --------------------------------------


def AES_encrypt(plain_text,key):
    f = Fernet(key)
    cipher_text = f.encrypt(plain_text.encode())
    return cipher_text.decode()


def AES_decrypt(cipher_text,key):
    f = Fernet(key)
    plain_text = f.decrypt(cipher_text.encode())
    return plain_text.decode()

#print ( AES_encrypt('hi',key) )
#>>> 'gAAAAABg7JMzIodK3VYYfGKsRi1e4HIbNSESfnLYcol6zMetrHU9NVwHdnVNpO_TXR1HcwOf7WjHSo-e2ryb_yayMdq4qjzAhg=='
#print( AES_decrypt(.....) )

