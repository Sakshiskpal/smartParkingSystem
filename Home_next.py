

from tkinter import *
import tkinter as tk
from tkintermapview import TkinterMapView
import main2
from booking import open_booking_page as open_booking


def booking():
    root.destroy()
    open_booking()

def available():
    root.destroy()
    main2.open_availability_page()

root = Tk()
root.title("Home Page")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)

#create header section
header = tk.Label(root, text='Smart Parking', bg='#445', height=1, width=250,
                  font=('Microsoft Yahei UI Light', 23, 'bold'), fg='white')
header.place(x=5, y=5)

# Create form elements
frame = Frame(root, width=650, height=700, border=1, bg='#fff')
frame.place(x=100, y=50)

map_widget = TkinterMapView(frame, width=350, height=400, corner_radius=0)  
map_widget.set_address("madhyapradesh, india")
map_widget.pack()

Button(width=29, pady=7, text='Booking', bg='#57a1f8', fg='white', border=0, command=booking).place(x=600, y=177)
Button(width=29, pady=7, text='Check Availability', bg='#57a1f8', fg='white', border=0, command=available).place(x=600, y=227)

root.mainloop()
