# gui_components.py

import tkinter as tk
from config import font_name, font_size, my_color

# Global variable to track the current answer window instance
current_answer_window = None


def start_quiz(root, quiz_instance):
    quiz_instance.start()
    answers = quiz_instance.fetch_q_and_a()
    create_answer_window(root, quiz_instance, answers)


def submit_answer(root, quiz_instance, user_answer_var):
    user_answer = user_answer_var.get()
    quiz_instance.submit()
    quiz_instance.check_user_answer(user_answer)
    quiz_instance.score_update(root)
    quiz_instance.game_over(root)
    answers = quiz_instance.fetch_q_and_a()
    if answers:
        create_answer_window(root, quiz_instance, answers)


def create_buttons(root, quiz_instance):
    start_btn = tk.Button(root, text="Start", command=lambda: start_quiz(root, quiz_instance))
    start_btn.config(font=(font_name, font_size))
    start_btn.place(x=505, y=50, width=75)

    submit_btn = tk.Button(root, text="Submit",
                           command=lambda: submit_answer(root, quiz_instance, root.user_answer_var))
    submit_btn.config(font=(font_name, font_size))
    submit_btn.place(x=405, y=50, width=75)

    quit_btn = tk.Button(root, text="Quit", bg='red', command=root.quit)
    quit_btn.config(font=(font_name, font_size))
    quit_btn.place(x=595, y=50, width=75)


def create_answer_window(root, quiz_instance, answers):
    global current_answer_window

    # Close the previous answer window if it exists
    if current_answer_window:
        current_answer_window.destroy()

    # Create a new answer window
    answer_win = tk.Toplevel(root)
    answer_win.title("Answers")
    answer_win.geometry("200x280+590+320")
    answer_win.config(bg='#e6e600')
    current_answer_window = answer_win

    # Instructional label at the top
    label = tk.Label(answer_win, text="Select Answer\nand\nClick Submit Button", font=(font_name, font_size))
    label.pack(ipadx=90, ipady=10)

    # Variable to store user answer selection
    user_answer_var = tk.StringVar()
    for answer in answers:
        btn = tk.Radiobutton(answer_win, text=answer, variable=user_answer_var, value=answer, indicator=0,
                             bg=my_color[2])
        btn.pack(ipadx=90, ipady=5, padx=2, pady=2)

    # Question number label at the bottom
    question_number_label = tk.Label(answer_win, text=f"Question Number: {quiz_instance.count}",
                                     font=(font_name, font_size))
    question_number_label.pack(side=tk.BOTTOM, ipadx=90, ipady=10)

    # Attach user answer variable to root for easy access in the submit button
    root.user_answer_var = user_answer_var
