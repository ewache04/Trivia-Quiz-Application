# main.py

import tkinter as tk
from config import my_color
from quiz import Quiz
from gui_components import create_buttons

root = tk.Tk()
root.title("Trivia Quiz")
root.geometry("700x600")
root.maxsize(700, 600)
root.config(bg=my_color[4])

text_widget = tk.Text(root, height=35, width=45, font=('Times New Roman', 12), padx=12, pady=12)
text_widget.pack(side=tk.LEFT, padx=10, pady=50)

scrollbar = tk.Scrollbar(root, command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)

quiz_instance = Quiz(text_widget)
quiz_instance.get_file()

create_buttons(root, quiz_instance)

root.mainloop()
