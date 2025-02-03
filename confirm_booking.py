import tkinter as tk

def open_confirm_booking_page(booked_slot):
    root = tk.Tk()
    root.title("Booking Confirmation")
    root.geometry("300x150")

    label = tk.Label(root, text="Booking Confirmation")
    label.pack(pady=10)

    slot_label = tk.Label(root, text=f"Booked Slot: {booked_slot}")
    slot_label.pack()

    button = tk.Button(root, text="Close", command=root.destroy)
    button.pack(pady=10)

    root.mainloop()
