choice_test_page_frame = None

def switch_to_choice_test_page(cur_page):
    # TODO : implement choice test
    # print("choice test")
    # messagebox.showinfo("choice_test", "choice test is still working!")
    cur_page.pack_forget()
    choice_test_page_frame.pack()

def next_callback():
    # TODO : implement next callback
    print("next button press")
    messagebox.showinfo("next", "next callback is still working!")

def answer_callback(answer_no):
    # TODO : implement answer callback
    print(f"answer number : {answer_no}")
    messagebox.showinfo("answer", "answer callback is still working!")

def choice_test_page_init():
    global choice_test_page_frame

    choice_test_page_frame = tk.Frame(gui.root)

    question_no_label = tk.Label(choice_test_page_frame, text="1/10", font=gui.custom_font)
    question_no_label.pack(pady=10)

    question_label = tk.Label(choice_test_page_frame, text="question", font=gui.custom_font)
    question_label.pack(pady=10)

    answer_1 = tk.Button(choice_test_page_frame, text="answer 1", command=lambda: answer_callback(1), font=gui.custom_font)
    answer_1.pack(pady=10)

    answer_2 = tk.Button(choice_test_page_frame, text="answer 2", command=lambda: answer_callback(2), font=gui.custom_font)
    answer_2.pack(pady=10)

    answer_3 = tk.Button(choice_test_page_frame, text="answer 3", command=lambda: answer_callback(3), font=gui.custom_font)
    answer_3.pack(pady=10)

    answer_4 = tk.Button(choice_test_page_frame, text="answer 4", command=lambda: answer_callback(4), font=gui.custom_font)
    answer_4.pack(pady=10)

    next_btn = tk.Button(choice_test_page_frame, text="next", command=next_callback, font=gui.custom_font)
    next_btn.pack(pady=10)

    back_btn = tk.Button(choice_test_page_frame, text="back", command=lambda: tp.switch_to_test_page(choice_test_page_frame), font=gui.custom_font)
    back_btn.pack(pady=10)

import tkinter as tk
import gui.gui as gui
import gui.test_page as tp
from tkinter import messagebox
