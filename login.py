#import necessary libraries
import tkinter as tk
from tkinter import ttk
import sqlite3
import random
from tkinter import *
from tkinter import messagebox
import os

from createaccount import *
from gui import *

db = sqlite3.connect('database.db')
cursor = db.cursor()

def loginscreen():

  # builds internal screen
  def login():
    user = username.get()
    passw = pasword.get()

    cursor.execute(
        f"SELECT fn FROM database WHERE username = '{user}' AND password = '{passw}'"
    )
    name = cursor.fetchone()

    if name:
      name = str(name)
      name = name[2:len(name)-3]
      backend(name)
    else:
      messagebox.showinfo("Please try again", "Your username and password do not match any existing accounts")
  # ------------------------------------------


  #Log In Screen
  root = Tk()
  root.geometry("700x400")

  root.title("Sign-in or Create an Account")

  L1 = Label(root, text="Username: ")
  L1.grid(row=0, column=0)


  L2 = Label(root, text="Password: ")
  
  L2.grid(row=1, column=0)



  e1 = StringVar()
  e2 = StringVar()


  username = Entry(root, textvariable=e1)
  username.grid(row=0, column=1)

  pasword = Entry(root, textvariable=e2, show="\u00B7")#masks password
  pasword.grid(row=1, column=1)

  lgn_button = Button(root, text="Login", command=lambda: login())
  lgn_button.grid(row=4, column=1)

  create_button = Button(root, text="Create new account", command=lambda: cw())
  create_button.grid(row=5, column=1)
  root.mainloop()