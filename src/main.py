import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random
import os

# Caminho base é a pasta onde o main.py está (ou seja, src)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho do Excel: src/data/questions.xlsx
excel_path = os.path.join(base_dir, 'data', 'questions.xlsx')

# Caminho do ícone: src/assets/icon.png
icon_path = os.path.join(base_dir, 'assets', 'icon.png')

# Verifica se os arquivos existem antes de abrir
print("Excel path:", excel_path)
print("Icon path:", icon_path)

df = pd.read_excel(excel_path)

janela = tk.Tk()
janela.title('Quiz')
janela.geometry('400x450')

# Aqui o ícone precisa ser criado DEPOIS do tkinter.Tk()
app_icon = PhotoImage(file=icon_path)
janela.iconphoto(False, app_icon)


#Pegar as perguntas aleatoriamente ------------------------------

questions = df.sample(n=10).values.tolist()

# Variaveis globais ------------------------------

score = 0
current_question = 0


# funçaõ verificar resposta -----------------------------------------

def check_answer(answer):
    global score, current_question

    if answer == correct_answer.get():
        score += 1
    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        show_result()


# função exibir próxima pergunta -------------------------------------------------------------

def display_question():
    question, option1, option2, option3, option4, answer = questions[current_question]
    question_label.config(text=question)

    correct_answer.set(answer)

    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda: check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda: check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda: check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda: check_answer(4))



# função para exibir o resultado final ------------------------------------------

def show_result():
    messagebox.showinfo("Quiz Finalizado", f"Parabéns! Você completou o quiz.\n\nPontuação final: {score}/{len(questions)}")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)

    play_again_btn.pack()

# função para jogar novamente

def play_again():
    global score, current_question

    score = 0
    current_question = 0
    random.shuffle(questions)

    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)

    play_again_btn.pack_forget()


#Definindo as cores para o projeto -----------------------------
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
button_text_color = "#FFFFFF"

janela.config(bg=background_color)
janela.option_add('*Font', 'Arial')


# Icon na tela ---------------------------------------------------

app_icon = PhotoImage(file='assets/icon.png')
app_label = tk.Label(janela, image = app_icon, bg = background_color)
app_label.pack(pady = 10)

# Componentes da interface ------------------------------------------

question_label = tk.Label(janela, text = "", wraplength=380, bg = background_color, fg = text_color, font = ("Arial", 12, "bold"))
question_label.pack(pady = 20)

correct_answer = tk.IntVar()

option1_btn = tk.Button(janela, text = "", width = 30, bg = button_color, fg = button_text_color, state = tk.DISABLED, font = ("Arial", 10, "bold"))
option1_btn.pack(pady = 10)

option2_btn = tk.Button(janela, text = "", width = 30, bg = button_color, fg = button_text_color, state = tk.DISABLED, font = ("Arial", 10, "bold"))
option2_btn.pack(pady = 10)

option3_btn = tk.Button(janela, text = "", width = 30, bg = button_color, fg = button_text_color, state = tk.DISABLED, font = ("Arial", 10, "bold"))
option3_btn.pack(pady = 10)

option4_btn = tk.Button(janela, text = "", width = 30, bg = button_color, fg = button_text_color, state = tk.DISABLED, font = ("Arial", 10, "bold"))
option4_btn.pack(pady = 10)


play_again_btn = tk.Button(janela, command = play_again, text = "Jogar Novamente", width = 30, bg = "#FF4500", fg = button_text_color, font = ("Arial", 10, "bold"))


display_question()


janela.mainloop()