# quiz.py

import random
import tkinter as tk


class Quiz:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.count = 0
        self.index_num = 0
        self.user_score = 0
        self.user_answer = [0]
        self.computer_score = 0
        self.activate_button = 0

    def get_file(self):
        self.file_name = 'q_a.txt'
        with open(self.file_name, 'r') as file:
            self.file_content = file.readlines()
        random.shuffle(self.file_content)

    def start(self):
        self.text_widget.config(state=tk.NORMAL)  # Make text widget editable for the game
        self.text_widget.delete('1.0', tk.END)
        self.index_num = 0
        self.activate_button = 1

    def submit(self):
        self.index_num += 1

    def fetch_q_and_a(self):
        if not self.activate_button:
            return None

        self.count = self.index_num + 1
        question_data = self.file_content[self.index_num].split('#')
        self.question = question_data[0].strip()
        self.correct_answer = question_data[1].strip().lower()

        self.text_widget.insert(tk.END, f"Q{self.count}: {self.question}\n\n")

        # Prepare answer options
        self.answer_pool = list(set(random.sample(range(10, 2020), 3)) | {self.correct_answer})
        random.shuffle(self.answer_pool)
        return self.answer_pool

    def check_user_answer(self, user_answer):
        if user_answer.lower() == self.correct_answer:
            self.user_score += 1
            result_text = 'Correct!\n'
        else:
            self.computer_score += 1
            result_text = f'Wrong! The correct answer was: {self.correct_answer}\n'

        self.text_widget.insert(tk.END, result_text + "\n")

    def score_update(self, root):
        tk.Label(root, text=f'Total Attempts: {self.count}', font=('Times New Roman', 12)).place(x=10, y=10)
        tk.Label(root, text=f'User Score: {self.user_score}', font=('Times New Roman', 12)).place(x=140, y=10)
        tk.Label(root, text=f'Computer Score: {self.computer_score}', font=('Times New Roman', 12)).place(x=270, y=10)

    def game_over(self, root):
        if self.user_score >= 10:
            msg = 'Game Over! You Won!'
        elif self.computer_score >= 5:
            msg = 'Game Over! You Lost!'
        else:
            return

        tk.Label(root, text=msg, font=('Times New Roman', 12), fg='red').place(x=470, y=10)

        # Display final summary
        self.display_summary()

        # Reset game values to default
        self.reset_to_default()

    def display_summary(self):
        # Clear and make text widget non-editable for summary
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete('1.0', tk.END)

        # Insert summary content
        summary_text = (
            "Game Summary:\n"
            f"Total Questions Attempted: {self.count}\n"
            f"User Score: {self.user_score}\n"
            f"Computer Score: {self.computer_score}\n"
        )

        self.text_widget.insert(tk.END, summary_text)

        # Make the text widget read-only
        self.text_widget.config(state=tk.DISABLED)

    def reset_to_default(self):
        self.count = self.index_num = self.user_score = self.computer_score = 0
        self.user_answer = [0]
        self.activate_button = 0
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete('1.0', tk.END)
