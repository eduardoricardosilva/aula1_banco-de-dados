import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def abrir_consulta(container):
    # Criar nova janela
    janela_consulta = tk.Toplevel(container)
    janela_consulta.title("Consulta de Livros")
    janela_consulta.geometry("600x400")
    janela_consulta.configure(bg="#e8f0f6")


    #titulo da janela
    tk.Label(janela_consulta, text="Consulta de Livros",font=("Segoe UI", 25, "bold"), bg="#e8f0f6").pack(pady=10)

    #digitar o titulo do livro
    tk.Entry(janela_consulta,font=("Segoe UI", 10, "bold"),width=50).pack(pady=15)

    #selicionar o gênero
    ttk.Combobox(janela_consulta,text="Gênero",font=("Segoe UI", 10, "bold"),width=45).pack(pady=15)

    #selecionar autor
    ttk.Combobox(janela_consulta,text="Autor",font=("Segoe UI", 10, "bold"),width=45).pack(pady=15)


    tk.Button(janela_consulta, text="Consultar",bg="#4CAF50",fg="black",
    font=("Segoe UI", 11, "bold"),
    activebackground="#45a049",
    activeforeground="white",
    width=10,
    height=1,
    cursor="hand2",
    relief="flat",
    bd=0
    ).pack(pady=15)

    janela_consulta.mainloop()

#abrir_consulta()

        
