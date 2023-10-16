#import all neceassary libraries
from tkinter import *
import tkinter as tk
from tkinter import ttk

# builds the gui with client's name
def backend(name):
  inner = Tk()
  inner.title("Welcome " + name)
  inner.geometry("700x400")

  frame1 = tk.Frame(inner, borderwidth=0, relief='ridge')
  frame1.grid(row=0, column=0, padx=(150, 150), pady=(70, 70))
  frame2 = tk.Frame(inner, borderwidth=0, relief='ridge')
  frame2.grid(row=0, column=1, padx=(150, 150), pady=(70, 70))
  frame3 = tk.Frame(inner, borderwidth=0, relief='ridge')
  frame3.grid(row=1, column=0, padx=(150, 150), pady=(70, 70))
  frame4 = tk.Frame(inner, borderwidth=0, relief='ridge')
  frame4.grid(row=1, column=1, padx=(150, 150), pady=(70, 70))

  w1 = tk.Label(frame1, text ='Log', font = "90", fg="Navyblue")
  frame1.config(highlightbackground = "red", highlightcolor= "red")
  w1.grid(row=0, column=0)
  w1_1 = tk.Label(frame1, text ='Frame', font = "45", fg="Navyblue")
  w1_1.grid(row=1, column=0)

  w2 = tk.Label(frame2, text ='↑', font = "90",fg="Navyblue")
  w2.grid(row=0, column=0)
  w2_1 = tk.Label(frame2, text ='← →', font = "45", fg="Navyblue")
  w2_1.grid(row=1, column=0)
  w2_2 = tk.Label(frame2, text ='↓', font = "45", fg="Navyblue")
  w2_2.grid(row=2, column=0)

  w3 = tk.Label(frame3, text ='Video', font = "90",fg="Navyblue")
  w3.grid(row=0, column=0)
  w3_1 = tk.Label(frame3, text ='Feed', font = "45", fg="Navyblue")
  w3_1.grid(row=1, column=0)

  w4 = tk.Label(frame4, text ='Blank', font = "90",fg="Navyblue")
  w4.grid(row=0, column=0)
  w4_1 = tk.Label(frame4, text ='Space', font = "45", fg="Navyblue")
  w4_1.grid(row=1, column=0)

  inner.mainloop()