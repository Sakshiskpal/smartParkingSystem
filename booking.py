import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from confirm_booking import open_confirm_booking_page

class BookingPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Parking Slot Booking")
        self.root.geometry("400x200")

        self.label = tk.Label(self.root, text="Enter your details:")
        self.label.pack()

        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.vehicle_label = tk.Label(self.root, text="Vehicle Number:")
        self.vehicle_label.pack()
        self.vehicle_entry = tk.Entry(self.root)
        self.vehicle_entry.pack()

        self.book_button = tk.Button(self.root, text="Book Slot", command=self.book_slot)
        self.book_button.pack()

        self.back_button = tk.Button(self.root, text="\u21A9 Back", command=self.back_to_home)
        self.back_button.pack()

    def book_slot(self):
        name = self.name_entry.get()
        vehicle_number = self.vehicle_entry.get()

        if name.strip() and vehicle_number.strip():
            booked_slot = f"{name} - {vehicle_number}"
            open_confirm_booking_page(booked_slot)  # Open confirmation page with booked slot
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter valid details.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.vehicle_entry.delete(0, tk.END)

    def back_to_home(self):
        # Add functionality to go back to the home page here
        pass

def open_booking_page():
    root = tk.Tk()
    app = BookingPage(root)
    root.mainloop()

if __name__ == "__main__":
    open_booking_page()
