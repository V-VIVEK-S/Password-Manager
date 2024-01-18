from tkinter import *
import sqlite3

# GUI

win = Tk()
win.title("Password Manger")
win.geometry("1920x1080")
win.configure(bg="black")

# SQLite 3 Database

conn = sqlite3.connect("password.db")
c = conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS passwordmanager(
          name text NOT NULL,
          password text NOT NULL
    )
""")
name = StringVar()
passw = StringVar()
fetname = StringVar()

# Inserting Password into database
def insertpass():
    c.execute(f"INSERT INTO passwordmanager VALUES('{name.get()}','{passw.get()}')")
    conn.commit()
    conn.close

# Fetch Password from database
def fetchpass():
    fetchpasswin = Toplevel(win)
    fetchpasswin.geometry("1280x720")
    fetchpasswin.configure(bg="black")
    txt_output = Text(fetchpasswin, height=30, width=50)
    c.execute(f"SELECT * FROM passwordmanager WHERE name = '{fetname.get()}'")
    my_list = c.fetchall()
    if my_list is not None:
        txt_output.insert(END, my_list)
    else:
        txt_output.insert(END,"None")
    txt_output.pack(pady=30)
    conn.commit()
    conn.close
    

# Fetch Password Window
def fetch():
    fetch = Toplevel(win)
    fetch.geometry("1920x1080")
    fetch.configure(bg="black")
    master_password = Label(fetch,text="Enter the Name of the site",font=("Ariel",35),fg="white",bg="black")
    master_password.pack(pady=(200,50))
    master_entry = Entry(fetch,font=("Ariel",25), width=25,textvariable=fetname)
    master_entry.pack(pady=50)
    button1 = Button(fetch, text = 'Submit',font=("Ariel",20),bg="black",fg="white",command=fetchpass)
    button1.pack()

# Enter Password Window
def enter():
    enter = Toplevel(win)
    enter.geometry("1920x1080")
    enter.configure(bg="black")
    label2 = Label(enter,text="Enter new password",font=("Ariel",35),fg="white",bg="black")
    label2.pack(pady=(200,50))
    label3 = Label(enter,text="Enter Name: ",font=("Ariel",25),fg="white",bg="black")
    label3.pack()
    entry2 = Entry(enter,font=("Ariel",25),width=25,textvariable=name)
    entry2.pack(pady=10)
    label4 = Label(enter,text="Enter Password: ",font=("Ariel",25),fg="white",bg="black")
    label4.pack()
    entry3 = Entry(enter,font=("Ariel",25), width=25,textvariable=passw)
    entry3.pack(pady=10)
    button2 = Button(enter, text = 'Submit',font=("Ariel",20),bg="black",fg="white",command=insertpass)
    button2.pack()

# Main Window
l1 = Label(win,text = "Password Manager",font=("Arial",35),fg="white",bg="black")
l1.pack(pady=(100,0))
b1 = Button(win, text = 'Fetch Password',font=("Ariel",20),bg="black",fg="white",command=fetch)
b1.pack(side="left",padx=(200,0))
b1 = Button(win, text = 'Enter Password',font=("Ariel",20),bg="black",fg="white",command=enter)
b1.pack(side="right",padx=(0,200))
win.mainloop()