import tkinter as tk
from tkinter import messagebox
import sqlite3
from login import montar_tela_login
from principal import montar_tela_principal
# v--- Certifique-se que este arquivo/função existe


def validar_e_entrar(usuario, senha):
    try:
        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()
        # Verifica se a tabela existe para evitar erros no teste
        cursor.execute("SELECT * FROM user WHERE email = ? AND senha = ?", (usuario, senha))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            messagebox.showinfo("Login", "Sucesso!")
            # Em vez de destruir o root, limpe-o e chame a nova tela
            for widget in root.winfo_children():
                widget.destroy()
            montar_tela_principal(root) # Chame sua função aqui
            
        else:
            messagebox.showerror("Login", "E-mail ou senha inválidos!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar no banco: {e}")

# Início do programa
root = tk.Tk()
montar_tela_login(root, validar_e_entrar)
root.mainloop()