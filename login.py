import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("Tela de Login")
root.geometry("200x300")

def validar_login():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE email = ? and senha = ?", (email.get(),senha.get(),))
    resultado = cursor.fetchone()
    conn.close()
    if validar_login():
    messagebox.showinfo("Login", "Sucesso!")
    else:
    messagebox.showerror("Login", "E-mail ou senha inválidos!")
    return conn
    
        


tk.Label(root, text="Login", font=("Arial", 14, "bold")).grid(row=0, column=1, columnspan=2, pady=10)

tk.Label(root, text="E-mail",).grid(row=1, column=1, columnspan=10, pady=10)

email = tk.Entry(root)
email.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root,text="Senha").grid(row=3, column=1, columnspan=2, pady=10)

senha = tk.Entry(root)
senha.grid(row=4, column=1, columnspan=2, pady=10)

btn_entrar = tk.Button(root, text="Entrar", command=validar_login,bg="#49b429").grid(row=5, column=1, columnspan=2, pady=10)


root.mainloop()