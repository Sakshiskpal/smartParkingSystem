# from tkinter import *
# from tkinter import messagebox
# import mysql.connector
# import main2
# window = Tk()
# window.title("Login")
# window.geometry('925x500+300+200')
# window.configure(bg='#fff')
# window.resizable(False, False)

# def signup():
#     window.destroy()
#     import signup

# def login():
#     db_config = {
#         'host': 'localhost',
#         'user': 'root',
#         'port': '3307',  # Change port if necessary
#         'password': 'password',
#         'database': 'test'
#     }

#     username = user_entry.get()
#     password = password_entry.get()

#     if username == '' or password == '':
#         messagebox.showerror('Error', 'Username and Password are required.')
#     else:
#         try:
#             # Connect to the database
#             con = mysql.connector.connect(**db_config)
#             cursor = con.cursor()

#             # Check if the username and password match
#             query = "SELECT * FROM users WHERE username = %s AND password = %s"
#             cursor.execute(query, (username, password))
#             result = cursor.fetchall()

#             if len(result) > 0:
#                 messagebox.showinfo('Success', 'Login successful.')
#                 # import Home_next
#                 window.destroy()
#                 import main2
#                 # Add your code to navigate to the next page or perform further actions
                
#             else:
#                 messagebox.showerror('Error', 'Invalid username or password.')

#             con.close()

#         except mysql.connector.Error as err:
#             messagebox.showerror('Error', f'Error connecting to the database: {err}')

# # Create form elements
# frame = Frame(window, width=350, height=300, bg='#fff')
# frame.place(x=480, y=50)

# heading = Label(frame, text='Login', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 11))
# heading.place(x=150, y=5)

# # Username Entry
# def on_enter(e):
#     user_entry.delete(0, 'end')
# def on_leave(e):
#     if user_entry.get()=='':
#         user_entry.insert(0, 'User Email ID')  
        
# user_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
# user_entry.place(x=30, y=80)
# user_entry.insert(0, 'Username')
# user_entry.bind("<FocusIn>",on_enter)
# user_entry.bind("<FocusOut>",on_leave)
# Frame(frame, width =295, height =2, bg = 'black').place(x=25, y=107)

# # Password Entry
# def on_enter(e):
#     password_entry.delete(0, 'end')
# def on_leave(e):
#     if password_entry.get()=='':
#         password_entry.insert(0, 'Password')    
        
# password_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11), show='*')
# password_entry.place(x=30, y=150)
# password_entry.insert(0, 'Password')
# password_entry.bind("<FocusIn>",on_enter)
# password_entry.bind("<FocusOut>",on_leave)
# Frame(frame, width =295, height =2, bg = 'black').place(x=25, y=177)


# Button(frame, width=39, pady=7, text='Sign IN', bg='#57a1f8', fg='white', border=0, command=login).place(x=30, y=217)
# Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9)).place(x=90, y=270)
# Button(frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signup).place(x=200, y=270)
# window.mainloop()
from tkinter import *
from tkinter import messagebox
import mysql.connector
import main2  # Assuming this is the module to import for the next page

window = Tk()
window.title("Login")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

def signup():
    window.destroy()
    import signup

def next_page():
    window.destroy()
    import Home_next

def login():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'port': '3307',  # Change port if necessary
        'password': 'password',
        'database': 'test'
    }

    username = user_entry.get()
    password = password_entry.get()

    if username == '' or password == '':
        messagebox.showerror('Error', 'Username and Password are required.')
    else:
        try:
            # Connect to the database
            con = mysql.connector.connect(**db_config)
            cursor = con.cursor()

            # Check if the username and password match
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchall()

            if len(result) > 0:
                messagebox.showinfo('Success', 'Login successful.')
                # Open the next page after successful login
                next_page()
                # Call a function to open the next page
            else:
                messagebox.showerror('Error', 'Invalid username or password.')

            con.close()

        except mysql.connector.Error as err:
            messagebox.showerror('Error', f'Error connecting to the database: {err}')

# Create form elements
frame = Frame(window, width=350, height=300, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame, text='Login', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 11))
heading.place(x=150, y=5)

# Username Entry
def on_enter(e):
    user_entry.delete(0, 'end')
def on_leave(e):
    if user_entry.get()=='':
        user_entry.insert(0, 'User Email ID')  
        
user_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user_entry.place(x=30, y=80)
user_entry.insert(0, 'Username')
user_entry.bind("<FocusIn>",on_enter)
user_entry.bind("<FocusOut>",on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# Password Entry
def on_enter(e):
    password_entry.delete(0, 'end')
def on_leave(e):
    if password_entry.get()=='':
        password_entry.insert(0, 'Password')    
        
password_entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11), show='*')
password_entry.place(x=30, y=150)
password_entry.insert(0, 'Password')
password_entry.bind("<FocusIn>",on_enter)
password_entry.bind("<FocusOut>",on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign IN', bg='#57a1f8', fg='white', border=0, command=login).place(x=30, y=217)
Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9)).place(x=90, y=270)
Button(frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signup).place(x=200, y=270)

window.mainloop()
