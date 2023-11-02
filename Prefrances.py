from tkinter import *
from Encryptsetup import *
from Decryptsetup import *
def endingsChange(temp):
  with open ("endings.txt","r+")as ed:
    old = ed.read()
  with open ("endings.txt","w+") as ed:
    temp2 = old +"\n" +temp 
    ed.write(temp2)
  regeneratendings()
  regeneratendings2()
def Home ():
  SetUP()
  root3.destroy()
def home3():
  SetUP()
  root.destroy()
def Home2():
  from main import start
  start()
  root2.destroy()
def endingsChangeSetUp():
  global root3
  global root2
  root2.destroy()
  root3 = Tk()
  root3.title(".somthing - Prefrances")
  root3.geometry("300x120")
  label = Label (root3, text = ".somthing")
  label.config(font=('Helvetica bold underline',20))
  e2 = Entry(root3,width = 10, borderwidth = 3)
  e2.insert(0,".")
  label3 = Label(root3,text =  "Type a ending you wants\n to use, stick to text files")
  button = Button(root3, text = "Submit", command= lambda: endingsChange(e2.get()))
  button2 = Button(root3, text = "Home", command= Home)
  label.grid(row =0 ,column=0, columnspan=2 )
  e2.grid (row = 1, column= 0)
  label3.grid(row = 1, column= 2 )
  button.grid(row = 2, column= 0)
  button2.grid(row = 0, column= 2)
 
def path(path):
  with open ("defoltending.txt","w+")as d:
    d.write(path)
  
  
  

def Pathsetup():
  global root2
  global root
  root2.destroy()
  root = Tk()
  root.title(".somthing - Path")
  root.geometry("300x120")
  label = Label (root, text = "Path")
  label.config(font=('Helvetica bold underline',20))
  e2 = Entry(root,width = 10, borderwidth = 3)
  label3 = Label(root,text =  "Type a path that\n you want to use")
  button = Button(root, text = "Submit", command= lambda: path(e2.get()))
  button2 = Button(root, text = "Home", command= home3)
  label.grid(row =0 ,column=0, columnspan=2 )
  e2.grid (row = 1, column= 0)
  label3.grid(row = 1, column= 2 )
  button.grid(row = 2, column= 0)
  button2.grid(row = 0, column= 2)
 

def SetUP():
  global root2
  root2 = Tk()
  root2.title("Home - Prefrances")
  root2.geometry("150x100")
  label = Label (root2, text = "Home")
  label.config(font=('Helvetica bold underline',20))
  button = Button(root2, text = ".somthing", command= endingsChangeSetUp)
  button2 = Button(root2, text = "Path", command= Pathsetup)
  button3 = Button(root2, text = "Home", command= Home2)
  label.grid(row =0 ,column=0, columnspan=2 )
  button.grid(row =1 , column=0 )
  button2.grid(row =1 , column= 1)
  button3.grid(row = 2, column= 0, columnspan=2)