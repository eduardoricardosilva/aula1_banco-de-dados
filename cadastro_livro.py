import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import messagebox
import sqlite3

def janela_cadastro_livro(container):
    janela_cad_livros = tk.Toplevel(container)
    janela_cad_livros.title("Cadastro de livros")
    janela_cad_livros.geometry("500x500")
    janela_cad_livros.configure(bg="#e8f0f6")

    #Títiulo da janela
    tk.Label(janela_cad_livros, text="Cadastro de livros",font=("Segoe UI", 25, "bold"), bg="#e8f0f6").pack(pady=15)

    #nome do livro
    tk.Label(janela_cad_livros, text="Nome do Livro",font=("Segoe UI", 10), bg="#e8f0f6").pack(pady=15)
    tk.Entry(janela_cad_livros,font=("Segoe UI", 10, "bold"),width=33).pack()

    #adicionar autor
    tk.Label(janela_cad_livros, text="Selecione o autor",font=("Segoe UI", 10), bg="#e8f0f6").pack(pady=5)
    ttk.Combobox(janela_cad_livros,font=("Segoe UI", 10, "bold"),width=30).pack(pady=5)

    #adicionar editora
    tk.Label(janela_cad_livros, text="Selecione a editora",font=("Segoe UI", 10), bg="#e8f0f6").pack(pady=5)
    ttk.Combobox(janela_cad_livros,font=("Segoe UI", 10, "bold"),width=30).pack()

    #adcionar Gênero
    tk.Label(janela_cad_livros, text="Selecione o Gênero", font=("  Segoe UI", 10),bg="#e8f0f6").pack(pady=5) 
    ttk.Combobox(janela_cad_livros,font=("Segoe UI", 10, "bold"),width=30).pack(pady=5) 

    #ISBN
    tk.Label(janela_cad_livros, text="ISBN", font=("Segoe UI", 10),bg="#e8f0f6").pack(pady=5)
    tk.Entry(janela_cad_livros, font=("Segoe UI", 10)).pack(pady=5)


    tk.Button(janela_cad_livros, text="Cadastrar",bg="#4CAF50",fg="black",font=("Segoe UI", 10, "bold")).pack(pady=15)



    janela_cad_livros.mainloop()