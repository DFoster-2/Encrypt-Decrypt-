from cryptography.fernet import Fernet
def decrypt(info):
  file = info
  with open ("key.key", "rb") as keyFill:
    key = keyFill.read()
  f = Fernet(key)
  with open (file,"rb") as Td:
    old2= Td.read()
  
  decrypt = f.decrypt(old2)
  
  with open (file,"wb") as TD:
    TD.write(decrypt)