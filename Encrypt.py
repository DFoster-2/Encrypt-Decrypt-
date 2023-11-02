from cryptography.fernet import Fernet
def encrypt(info):
  file = info
  with open ("key.key", "rb") as keyFill:
    key = keyFill.read()
  
  f = Fernet(key)
  
  with open (file,"rb") as T:
    old = T.read()
  
  encrypt = f.encrypt(old)
  
  with open (file,"wb") as TC:
    TC.write(encrypt)
  