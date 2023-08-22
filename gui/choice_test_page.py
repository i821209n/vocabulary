choice_test_page_frame = None
question_num_label = None
question_label = None
next_btn = None
answer_1 = None
answer_2 = None
answer_3 = None
answer_4 = None
question_num = 1
total_words_num = 0
total_question_num = 0
question_pool = []
qid = 0
qa_dict = {}
right_answer = 0
default_color = None
bingo_color = "green"
wrong_color = "red"

def setup_ans_btn():
    global qa_dict, right_answer
    qa_dict = {}
    qa_list = [0, 0, 0, 0]
    num_to_ans_btn = {1:answer_1, 2:answer_2, 3:answer_3, 4:answer_4}
    right_answer = random.randint(1, 4)
    print(f"right answer = {right_answer}")
    for i in range(len(qa_list)):
        if (i+1 == right_answer):
            qa_list[i] = qid
            num_to_ans_btn[i+1].config(text=sheets.get_word(qa_list[i]))
            continue
        while True:
            ansId = random.randint(1, total_words_num)
            if (ansId != qid) and (ansId not in qa_list):
                qa_list[i] = ansId
                num_to_ans_btn[i+1].config(text=sheets.get_word(qa_list[i]))
                break
    
    print(qa_list)

def set_question():
    global qid
    num = len(question_pool)
    qid = question_pool[random.randint(0, num-1)]
    question = sheets.get_definition(qid)
    question_label.config(text=question)
    print(qid, question)
    question_pool.remove(qid)
    print(question_pool)

def set_qa():
    set_question()
    setup_ans_btn()  

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
    enableAllAnsBnt()
    question_init()
    set_qa()
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
    if(question_num < total_question_num):
        question_num += 1
        question_num_label.config(text=f"{question_num}/{total_question_num}")
        set_qa()
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
    global choice_test_page_frame, question_num_label, question_label, next_btn, answer_1, answer_2, answer_3, answer_4, default_color

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

    default_color = answer_1.cget("bg")
    print(default_color)

import tkinter as tk
import gui.gui as gui
import gui.test_page as tp
import sheets.sheets as sheets
import random
from tkinter import messagebox
