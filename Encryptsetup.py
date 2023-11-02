from tkinter import *
import os.path
def regeneratendings():
  with open("endings.txt", "r")as ed:
  	dta = ed.read()
  	endings = dta.split("\n")



def submit3(info,info2):
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
  global root2
  from main import start
  start()
  root2.destroy()
def setupE():
  global root2
  global endings
  global label2
  with open("endings.txt", "r")as ed:
  	dta = ed.read()
  	endings = dta.split("\n")
  
  root2 = Tk()
  root2.title("Encrypt")
  label = Label (root2, text = "Encrypt")
  label.config(font=('Helvetica bold underline',20))
  e2 = Entry(root2,width = 10, borderwidth = 3)
  button = Button(root2, text = "Submit", command= lambda: submit3(e2.get(),variable.get()) )
  variable = StringVar(root2)
  variable2 = StringVar(root2)

  variable.set(endings[0]) 
  w = OptionMenu(root2, variable, *endings) 

  label3 = Label(root2,text =  "If you want to set up\n a default\n path or add a ending \ngo to the menu \nand click preferences")
  label3.grid(row = 0,rowspan= 2, column= 2 )
  button2 =  Button(root2, text = "Home", command= home)
  button2.grid(row = 2, column= 2)
  
  label.grid(row = 0,column=0, columnspan= 2)
  e2.grid (row = 1, column= 0)
  button.grid(row = 2, column= 0)
  w.grid(row= 1, column= 1 )

  label2 = Label(root2, text = "")
  label2.grid(row= 3, column= 0)
  with open ("defoltending.txt","r+") as d:
    path = d.read()
    e2.insert(0,path)
  

  
