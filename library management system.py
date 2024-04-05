import tkinter as tk
from tkinter import messagebox
import csv

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    with open('books.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, isbn])
    messagebox.showinfo("Success", "Book added successfully!")

def display_books():
    book_listbox.delete(0, tk.END)
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            book_listbox.insert(tk.END, f"{row[0]} - {row[1]} ({row[2]})")

# Create GUI
root = tk.Tk()
root.title("Library Management System")

# Labels
title_label = tk.Label(root, text="Title:")
title_label.grid(row=0, column=0)
author_label = tk.Label(root, text="Author:")
author_label.grid(row=1, column=0)
isbn_label = tk.Label(root, text="ISBN:")
isbn_label.grid(row=2, column=0)

# Entry widgets
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)
author_entry = tk.Entry(root)
author_entry.grid(row=1, column=1)
isbn_entry = tk.Entry(root)
isbn_entry.grid(row=2, column=1)

# Buttons
add_button = tk.Button(root, text="Add Book", command=add_book)
add_button.grid(row=3, column=0, columnspan=2, pady=10)
display_button = tk.Button(root, text="Display Books", command=display_books)
display_button.grid(row=4, column=0, columnspan=2)

# Listbox
book_listbox = tk.Listbox(root)
book_listbox.grid(row=5, column=0, columnspan=2)

root.mainloop()