from tkinter import *
def submit2(Encrypt_Decrypt):
  global root

  #Encrypt_Decrypt = e.get()
  Encrypt_Decrypt = Encrypt_Decrypt.lower()
  if Encrypt_Decrypt == "encrypt":
    from Encryptsetup import setupE
    setupE()
    root.destroy()
  elif Encrypt_Decrypt == "decrypt":
    from Decryptsetup import setupD
    setupD()
    root.destroy()
  elif Encrypt_Decrypt== "word":
    from Word import start2
    start2()
    root.destroy()
  elif Encrypt_Decrypt== "prefrances":
    from Prefrances import SetUP
    SetUP()
    root.destroy()
  else:
    label2= Label(root, text = "Not an opshion")
    label2.grid(row = 4, column= 0)

def start():
  global root
  root = Tk()
  root.title("Menu")
  label = Label (root, text = "Encrypt/Decrypt/\nWord/Preferences:")
  label.config(font=('Helvetica bold underline',20))
  e = Entry(root,width = 10, borderwidth = 3)
  button = Button(root, text = "Submit", command= lambda: submit2(e.get()) )
  label.grid(row = 1,column=0)
  e.grid (row = 2, column= 0)
  button.grid(row = 3, column= 0)
  
from login import login
login()
start()

#from Decrypt import *
#from Word import start2
#start2()
