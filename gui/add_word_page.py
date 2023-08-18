add_word_page_frame = None

def switch_to_add_word_page(cur_page):
    sheets.add_word_sheet_init()
    cur_page.pack_forget()
    add_word_page_frame.pack()

def save_word(word_entry, definition_entry, sentence_entry):
    word = word_entry.get()
    definition = definition_entry.get()
    sentence = sentence_entry.get()
    if(word == ""):
        messagebox.showwarning("Warning", "Please enter a word.")
    elif(definition == ""):
        messagebox.showwarning("Warning", "Please enter the definition.")
    elif(sentence == ""):
        messagebox.showwarning("Warning", "Please enter a sentence.")
    else:
        sheets.save_word(word, definition, sentence)
        print("save the word!!")
        messagebox.showinfo("Saving", f"save {word} success")
        word_entry.delete(0, tk.END)
        definition_entry.delete(0, tk.END)
        sentence_entry.delete(0, tk.END)

def add_word_page_init():
    global add_word_page_frame

    add_word_page_frame = tk.Frame(gui.root)
    # add_word_page_frame.pack()

    word_label = tk.Label(add_word_page_frame, text="Enter a word:", font=gui.custom_font)
    word_label.pack(pady=10)

    word_entry = tk.Entry(add_word_page_frame, font=gui.custom_font, width=60)
    word_entry.pack(pady=5)

    definition_label = tk.Label(add_word_page_frame, text="Enter the definition:", font=gui.custom_font)
    definition_label.pack(pady=10)

    definition_entry = tk.Entry(add_word_page_frame, font=gui.custom_font, width=60)
    definition_entry.pack(pady=5)

    sentence_label = tk.Label(add_word_page_frame, text="Enter a example:", font=gui.custom_font)
    sentence_label.pack(pady=10)

    sentence_entry = tk.Entry(add_word_page_frame, font=gui.custom_font, width=60)
    sentence_entry.pack(pady=5)

    save_btn = tk.Button(add_word_page_frame, text="save", command=lambda: save_word(word_entry, definition_entry, sentence_entry), font=gui.custom_font)
    save_btn.pack(pady=10)

    back_btn = tk.Button(add_word_page_frame, text="back", command=lambda: fp.switch_to_first_page(add_word_page_frame), font=gui.custom_font)
    back_btn.pack(pady=10)

import tkinter as tk
import gui.gui as gui
import sheets.sheets as sheets
import gui.first_page as fp
from tkinter import messagebox
