#import
import tkinter as tk
from tkinter import font
from tkinter import messagebox
import sheets

#variables
root = None
custom_font = None
first_page_frame = None
add_word_page_frame = None
test_page_frame = None
calendar_page_frame = None

#apis
def switch_to_adding_word_page():
    sheets.add_word_sheet_init()
    first_page_frame.pack_forget()
    add_word_page_frame.pack()

def switch_to_testing_page():
    first_page_frame.pack_forget()
    test_page_frame.pack()

def switch_to_calendar_page():
    # TODO : implement calendar page
    print("calendar page")
    messagebox.showinfo("calendar_page", "calendar page is still working!")

def switch_to_first_page(cur_page):
    cur_page.pack_forget()
    first_page_frame.pack()

def switch_to_choice_test_page():
    # TODO : implement choice test
    print("choice test")
    messagebox.showinfo("choice_test", "choice test is still working!")

def switch_to_spell_test_page():
    # TODO : implement spell test
    print("spell test")
    messagebox.showinfo("spell_test", "spell test is still working!")

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
        # TODO : implement save words to google sheets
        sheets.save_word(word, definition, sentence)
        print("save the word!!")
        messagebox.showinfo("Saving", f"save {word} success")
        word_entry.delete(0, tk.END)
        definition_entry.delete(0, tk.END)
        sentence_entry.delete(0, tk.END)

def first_page_init():
    global first_page_frame

    first_page_frame = tk.Frame(root)
    # first_page_frame.pack()

    adding_word_btn = tk.Button(first_page_frame, text="add words", command=switch_to_adding_word_page, font=custom_font)
    adding_word_btn.pack(pady=10)

    testing_btn = tk.Button(first_page_frame, text="test", command=switch_to_testing_page, font=custom_font)
    testing_btn.pack(pady=10)

    calendar_btn = tk.Button(first_page_frame, text="calendar", command=switch_to_calendar_page, font=custom_font)
    calendar_btn.pack(pady=10)

def add_word_page_init():
    global add_word_page_frame

    add_word_page_frame = tk.Frame(root)
    # add_word_page_frame.pack()

    word_label = tk.Label(add_word_page_frame, text="Enter a word:", font=custom_font)
    word_label.pack(pady=10)

    word_entry = tk.Entry(add_word_page_frame, font=custom_font, width=60)
    word_entry.pack(pady=5)

    definition_label = tk.Label(add_word_page_frame, text="Enter the definition:", font=custom_font)
    definition_label.pack(pady=10)

    definition_entry = tk.Entry(add_word_page_frame, font=custom_font, width=60)
    definition_entry.pack(pady=5)

    sentence_label = tk.Label(add_word_page_frame, text="Enter a example:", font=custom_font)
    sentence_label.pack(pady=10)

    sentence_entry = tk.Entry(add_word_page_frame, font=custom_font, width=60)
    sentence_entry.pack(pady=5)

    save_btn = tk.Button(add_word_page_frame, text="save", command=lambda: save_word(word_entry, definition_entry, sentence_entry), font=custom_font)
    save_btn.pack(pady=10)

    back_btn = tk.Button(add_word_page_frame, text="back", command=lambda: switch_to_first_page(add_word_page_frame), font=custom_font)
    back_btn.pack(pady=10)

def test_page_init():
    global test_page_frame

    test_page_frame = tk.Frame(root)

    choice_test = tk.Button(test_page_frame, text="choice test", command=switch_to_choice_test_page, font=custom_font)
    choice_test.pack(pady=10)

    spell_test = tk.Button(test_page_frame, text="spell test", command=switch_to_spell_test_page, font=custom_font)
    spell_test.pack(pady=10)

    back_btn = tk.Button(test_page_frame, text="back", command=lambda: switch_to_first_page(test_page_frame), font=custom_font)
    back_btn.pack(pady=10)

def gui_init():
    global root, custom_font

    root = tk.Tk()
    root.title("Vocabulary Application")

    window_width = 800
    window_height = 600
    root.geometry(f"{window_width}x{window_height}")

    custom_font = font.Font(size=20)

    # first page
    first_page_init()
    # add word page 
    add_word_page_init()
    # test page
    test_page_init()

    # Show first page initially
    first_page_frame.pack()

    root.mainloop()