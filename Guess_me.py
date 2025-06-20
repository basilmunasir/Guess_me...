import tkinter as tk

frame = tk.Tk()
frame.title("Guess me...")
frame.geometry("400x300")

label=tk.Label(frame,text="I Guessed a number between 1 and 50\nCan you predict it??\nYou Got 5 try",fg="white",bg="black",font=("Times New Roman",16))
label.place(x=10,y=10,width=380,height=100)

sevenbutton=tk.Button(frame,text="7",fg="red",bg="light grey",font=("Times New Roman",16))
sevenbutton.place(x=10,y=120,width=120,height=35,)

eightbutton=tk.Button(frame,text="8",fg="red",bg="light grey",font=("Times New Roman",16))
eightbutton.place(x=140,y=120,width=120,height=35)

ninebutton=tk.Button(frame,text="9",fg="red",bg="light grey",font=("Times New Roman",16))
ninebutton.place(x=270,y=120,width=120,height=35)


fourbutton=tk.Button(frame,text="4",fg="red",bg="light grey",font=("Times New Roman",16))
fourbutton.place(x=10,y=165,width=120,height=35)

fivebutton=tk.Button(frame,text="5",fg="red",bg="light grey",font=("Times New Roman",16))
fivebutton.place(x=140,y=165,width=120,height=35)

sixbutton=tk.Button(frame,text="6",fg="red",bg="light grey",font=("Times New Roman",16))
sixbutton.place(x=270,y=165,width=120,height=35)


onebutton=tk.Button(frame,text="1",fg="red",bg="light grey",font=("Times New Roman",16))
onebutton.place(x=10,y=210,width=120,height=35)

twobutton=tk.Button(frame,text="2",fg="red",bg="light grey",font=("Times New Roman",16))
twobutton.place(x=140,y=210,width=120,height=35)

threebutton=tk.Button(frame,text="3",fg="red",bg="light grey",font=("Times New Roman",16))
threebutton.place(x=270,y=210,width=120,height=35)

zerobutton=tk.Button(frame,text="0",fg="red",bg="light grey",font=("Times New Roman",16))
zerobutton.place(x=10,y=255,width=120,height=35)

enterbutton=tk.Button(frame,text="Enter",fg="red",bg="light grey",font=("Times New Roman",16))
enterbutton.place(x=140,y=255,width=250,height=35)




frame.mainloop()