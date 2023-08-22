choice_test_page_frame = None
question_num_label = None
next_btn = None
answer_1 = None
answer_2 = None
answer_3 = None
answer_4 = None
question_num = 1
total_words_num = 0
total_question_num = 0
question_pool = []

def question_init():
    global question_pool
    question_pool = []
    for i in range(total_question_num):
        question_pool.append(i+1)
    print(question_pool)

def switch_to_choice_test_page(cur_page):
    global question_num, total_words_num, total_question_num
    # TODO : implement choice test
    total_words_num = sheets.get_word_num()
    if(total_words_num == 0):
        messagebox.showinfo("choice test", "no word is availble")
        return
    elif(total_words_num > 10):
        total_question_num = 10
    else:
        total_question_num = total_words_num
    question_num = 1
    question_num_label.config(text=f"{question_num}/{total_question_num}")
    next_btn.config(state="disabled", text="next")
    question_init()
    cur_page.pack_forget()
    choice_test_page_frame.pack()

def disableAllAnsBnt():
    answer_1.config(state="disabled")
    answer_2.config(state="disabled")
    answer_3.config(state="disabled")
    answer_4.config(state="disabled")

def enableAllAnsBnt():
    answer_1.config(state="normal")
    answer_2.config(state="normal")
    answer_3.config(state="normal")
    answer_4.config(state="normal")

def next_callback():
    # TODO : implement next callback
    global question_num
    next_btn.config(state="disabled")
    enableAllAnsBnt()
    if(question_num < 10):
        question_num += 1
        question_num_label.config(text=f"{question_num}/{total_question_num}")
    else:
        messagebox.showinfo("done", "test done return to test page")
        tp.switch_to_test_page(choice_test_page_frame)
    print("next button press")
    
def answer_callback(answer_num):
    # TODO : implement answer callback
    next_btn.config(state="normal")
    disableAllAnsBnt()
    if(question_num == 10):
        next_btn.config(text="done")
    print(f"answer number : {answer_num}")
    # messagebox.showinfo("answer", "answer callback is still working!")

def choice_test_page_init():
    global choice_test_page_frame, question_num_label, next_btn, answer_1, answer_2, answer_3, answer_4

    choice_test_page_frame = tk.Frame(gui.root)

    # question_num_label = tk.Label(choice_test_page_frame, text="1/10", font=gui.custom_font)
    question_num_label = tk.Label(choice_test_page_frame, font=gui.custom_font)
    question_num_label.pack(pady=10)

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
import sheets.sheets as sheets
from tkinter import messagebox
