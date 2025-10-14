import os
import sys


import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
import json
import random

# Função para centralizar a janela na tela
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# Função para mostrar a pergunta
def show_question(root, question_data, user_name, score_label, unanswered_questions):
    question = question_data["question"]
    options = question_data["options"]
    correct_answer = question_data["correct_answer"]

    root.title("Pergunta")
    
    # Label para o nome do usuário
    question_user = tk.Label(root, text='Nome: ' + user_name, wraplength=300, padx=100, pady=0)
    question_user.pack()
    
    if sys.platform == "win32":
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    
    # Label para a pontuação
    question_score = tk.Label(root, text='Pontos: ' + str(score_label.get()), wraplength=300, padx=100, pady=0)
    question_score.pack()
    
    # Label para a pergunta
    question_label = tk.Label(root, text=question, wraplength=300, padx=10, pady=10)
    question_label.pack()
    
    # Função para lidar com a seleção de resposta
    def handle_response(option):
        if option == correct_answer:
            messagebox.showinfo("Resposta correta", "Resposta correta! +1 ponto!")
            score_label.set(score_label.get() + 1)
        else:
            messagebox.showerror("Resposta incorreta", f"Resposta errada! -3 pontos! A resposta correta é: {correct_answer}")
            score_label.set(score_label.get() - 3)

        # Atualizar a pontuação na tela
        question_score.config(text='Pontos: ' + str(score_label.get()))

        # Destruir a janela atual
        root.destroy()

        # Exibir a próxima pergunta
        if unanswered_questions:
            show_question(tk.Tk(), unanswered_questions.pop(0), user_name, score_label, unanswered_questions)
        else:
            # Todas as perguntas foram respondidas
            save_score(score_label.get())
            messagebox.showinfo("Pontuação final", f"{user_name}, Pontuação Final: {score_label.get()}")
            root.quit()

    # Função para salvar a pontuação ao fechar a janela
    def on_closing():
        save_score(score_label.get())
        root.destroy()

    # Vinculando a função de fechamento ao evento de fechamento da janela
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Criando botões para cada opção de resposta
    for option in options:
        
        def on_enter(e):
            e.widget['background'] = 'green'

        def on_leave(e):
            e.widget['background'] = 'black'
            
        frame = tk.Frame(root, bd=1)
        frame.pack(pady=5, padx=10, fill="x")

        message = tk.Message(frame, text=option, width=300, justify="left")
        message.pack(side="left", padx=5)
        
        # Criando um botão com bordas arredondadas
        button2 = tk.Button(frame, text="Selecionar", command=lambda o=option: handle_response(o), padx=10, pady=5, relief="groove", font=("Arial", 10, "bold"), cursor="hand2")
        button2.pack(side="right", padx=5)
        
        button2.bind("<Enter>", on_enter)
        button2.bind("<Leave>", on_leave)

    # Centralizando a janela
    center_window(root)
        
# Funções para carregar e salvar dados
def load_user_name():
    try:
        with open("user_name.txt", "r", encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def save_user_name(name):
    with open("user_name.txt", "w", encoding='utf-8') as file:
        file.write(name)

def load_score():
    try:
        with open("score.txt", "r", encoding='utf-8') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0

def save_score(score):
    with open("score.txt", "w", encoding='utf-8') as file:
        file.write(str(score))

def load_questions():
    try:
        with open("questions.json", "r", encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_questions(questions):
    with open("questions.json", "w", encoding='utf-8') as file:
        json.dump(questions, file, ensure_ascii=False, indent=4)

def filter_questions_by_category(questions, category):
    if category == "Geral":
        return questions
    else:
        return [q for q in questions if q.get("category") == category]

# Solicitar o nome do usuário se não estiver salvo
user_name = load_user_name()
if user_name is None:
    user_name = input("Por favor, digite seu nome: ")
    save_user_name(user_name)

# Verificando se há perguntas não respondidas
questions = load_questions()
if not questions:
    print("Não há perguntas disponíveis.")
    exit()

# Criando a janela principal
root = tk.Tk()
style = Style(theme='flatly')  # Escolha do tema do ttkbootstrap

# Função para selecionar a categoria
def select_category(category):
    unanswered_questions = filter_questions_by_category(questions, category)
    if not unanswered_questions:
        print("Não há perguntas disponíveis para a categoria selecionada.")
        exit()
    for q in unanswered_questions:
        q["answered"] = False
    random.shuffle(unanswered_questions)
    
    global score
    # Criando a variável de controle para a pontuação
    score = tk.IntVar()
    score.set(load_score())
    
    # Exibir a primeira pergunta
    show_question(tk.Tk(), unanswered_questions.pop(0), user_name, score, unanswered_questions)
    root.destroy()

# Janela de seleção de categoria
category_label = tk.Label(root, text="Selecione a categoria:", wraplength=300, padx=10, pady=10)
category_label.pack()

categories = ["Geral", "Estoque", "PDV"]
for category in categories:
    button = ttk.Button(root, text=category, style="Outline.TButton", cursor="hand2", command=lambda c=category: select_category(c))
    button.pack(pady=5)

# Função para salvar a pontuação ao fechar a janela principal
def on_closing_main():
    save_score(score.get())
    root.destroy()

# Vinculando a função de fechamento ao evento de fechamento da janela principal
root.protocol("WM_DELETE_WINDOW", on_closing_main)

# Centralizando a janela principal
center_window(root)

# Iniciar o loop principal da aplicação
root.mainloop()