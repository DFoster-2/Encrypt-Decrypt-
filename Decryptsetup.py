from tkinter import *
import os.path
def regeneratendings2():
  with open("endings.txt", "r")as ed:
  	dta = ed.read()
  	endings = dta.split("\n")

def submit4(info, info2):
  global label2
  info12 = "/home/runner/Encrypt-Decrpt-V2/Files/"+ info +info2
  print (info12)
  yes = os.path.exists(info12)
  if yes == True:
    from Encrypt import encrypt
    encrypt(info12)
    label2.config(text = "")
  else:
    label2.config(text = "No such file")
def home():
  global root3
  from main import start
  start()
  root3.destroy()
def setupD():
  global label2
  global root3
  global endings2
  with open("endings.txt", "r")as ed:
  	dta = ed.read()
  	endings2 = dta.split("\n")
  root3 = Tk()
  root3.title("Decrypt")
  label = Label (root3, text = "Decrypt")
  label.config(font=('Helvetica bold underline',20))
  e2 = Entry(root3,width = 10, borderwidth = 3)
  button = Button(root3, text = "Submit", command= lambda: submit4(e2.get(),variable.get()) )
  variable = StringVar(root3)

  variable.set(endings2[0]) 
  w = OptionMenu(root3, variable, *endings2)
  label3 = Label(root3,text =  "If you want to set up\n a defolt\n path or add a ending \ngo to the menu \nand click preferences")
  label3.grid(row = 0,rowspan= 2, column= 2 )
  button2 =  Button(root3, text = "Home", command= home)
  button2.grid(row = 2, column= 2)
  
  
  label2 = Label(root3, text = "")
  label2.grid(row= 3, column= 0)
  
  label.grid(row = 0,column=0, columnspan= 2)
  e2.grid (row = 1, column= 0)
  button.grid(row = 2, column= 0)
  w.grid(row= 1, column= 1 )
