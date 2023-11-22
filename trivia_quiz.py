# Author: Jeremiah E. Ochepo# Date Written: 04/11/2020# Date Updated: 04/20/2020# Code Description: Trivia Quizimport randomfrom tkinter import *import tkinter as tk# Define a list of colors for the applicationmy_color = ['skyblue', 'red', 'light green', 'white', '#808000']# Question Windowroot = tk.Tk()root.title('Questions')root.geometry('700x600')root.maxsize(700, 600)root.config(bg=my_color[4])# Scrollbar and text decorationScrollbar = tk.Scrollbar(root)text = tk.Text(root, height=35, width=45)Scrollbar.config(command=text.yview)text.pack(side=tk.LEFT, padx=10, pady=50, fill=tk.Y)Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)text.config(padx=12, pady=12, font=('times New Roman', 12), yscrollcommand=Scrollbar.set)font_name = 'times New Roman'font_size = 12class Quiz:    def __init__(self, *args, **kwargs):        self.count = 0        self.index_num = 0        self.user_score = 0        self.user_answer = [0]        self.computer_score = 0        self.activate_button = 0    # Load questions and answers from a file    def get_file(self):        self.file_name = 'q_a.txt'        self.read_file = open(self.file_name, 'r')        self.file_content = self.read_file.readlines()        random.shuffle(self.file_content)    # Display the first question and activate the submit button    def start(self):        text.delete('0.0', "end")        self.index_num = 0        self.activate_button = 1        try:            game_over_label.destroy()        except:            pass    # Submit user's answer and display the next question    def submit(self):        self.index_num += 1    # Display question and multiple answers for users to select    def fetch_q_and_a(self):        if self.activate_button == 0:            pass        else:            self.count = self.index_num            self.count += 1            self.q_and_a = []            self.q_and_a = self.file_content            self.q_and_a = self.q_and_a[self.index_num].split('#')            self.question = self.q_and_a[0]            txt = f'{self.count} {self.question}'            text.insert(tk.END, f'{txt}\n')            text.pack()            self.correct_answer = str(self.q_and_a[1]).lower()            self.correct_answer = self.correct_answer.replace('\n', '')            print(self.correct_answer)            self.answer_pool = {}            self.answer_pool = set(random.sample(range(10, 2020), 3))            self.answer_pool.update([self.correct_answer])            self.answer_pool = list(self.answer_pool)            random.shuffle(self.answer_pool)            # Answer Window for displaying answer options            global win            win = tk.Tk()            win.title('Answers')            win.geometry('200x280+590+300')            win.maxsize(200, 280)            win.config(bg='#e6e600')            label = tk.Label(win, text='Select Answer\nand\nClick Submit Button')            label.pack(ipadx=90, ipady=10)            var = StringVar(win)            var.set("")            def user_selection():                self.user_answer.append(var.get())            for txt in self.answer_pool:                btn1 = tk.Radiobutton(win, text=txt, variable=var,                                      value=txt, indicator=0, command=lambda: user_selection())                btn1.config(bg=my_color[2])                btn1.pack(ipadx=90, ipady=5, padx=2, pady=2)            txt = f'Question Number  {self.count}'            label = tk.Label(win, text=txt)            label.pack(side=BOTTOM, ipadx=90, ipady=10)    # Verify user's answer    def check_user_answer(self):        try:            win.destroy()            self.user_answer = (self.user_answer[len(self.user_answer) - 1])            if self.user_answer == self.correct_answer:                self.user_score += 1                txt = 'Correct!\n'            else:                self.computer_score += 1                txt = f'Wrong!.\n'                txt += f'Correct answer : {self.correct_answer}.\n'            text.insert(tk.END, f'{txt}\n')            self.user_answer = [0]        except:            pass    # Update and display scores    def score_update(self):        label = tk.Label(root, text=f'Total attempt :  {self.count}')        label.config(font=(font_name, font_size))        label.place(x=10, y=10)        label = tk.Label(root, text=f'User score :  {self.user_score}')        label.config(font=(font_name, font_size))        label.place(x=140, y=10)        label = tk.Label(root, text=f'Computer score :  {self.computer_score}')        label.config(font=(font_name, font_size))        label.place(x=270, y=10)    # Display game over message    def game_over(self):        global game_over_label        x_coord = 470        y_coord = 10        try:            if self.user_score == 10:                game_over_msg = 'Game Over! You Won!'                quiz_info.reset_to_default()            elif self.computer_score == 5:                game_over_msg = 'Game Over! You Loss!'                quiz_info.reset_to_default()            game_over_label = tk.Label(root, text=game_over_msg)            game_over_label.config(font=(font_name, font_size))            game_over_label.place(x=x_coord, y=y_coord)        except:            pass    # Reset program to default values    def reset_to_default(self):        self.count = 0        self.index_num = 0        self.user_score = 0        self.user_answer = [0]        self.computer_score = 0        self.activate_button = 0        text.delete('0.0', "end")quiz_info = Quiz()quiz_info.get_file()def start_quiz():    quiz_info.start()    quiz_info.fetch_q_and_a()    submit_button()    quiz_info.score_update()    quiz_info.game_over()def submit_answer():    quiz_info.submit()    quiz_info.check_user_answer()    quiz_info.score_update()    quiz_info.game_over()    quiz_info.fetch_q_and_a()def start_button():    start_btn = tk.Button(root, text="Start", command=lambda: start_quiz())    start_btn.config(font=(font_name, font_size))    start_btn.place(x=505, y=50, width=75)start_button()def submit_button():    submit_btn = tk.Button(root, text="Submit", command=lambda: submit_answer())    submit_btn.config(font=(font_name, font_size))    submit_btn.place(x=405, y=50, width=75)submit_button()def quit_button():    quit_btn = tk.Button(root, text="Quit", bg='red', command=quit)    quit_btn.config(font=(font_name, font_size))    quit_btn.place(x=595, y=50, width=75)quit_button()root.mainloop()