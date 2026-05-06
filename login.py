import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("Tela de Login")
root.geometry("350x350")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(8, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(4, weight=1)

def validar_login():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user WHERE email = ? and senha = ?", (email.get(),senha.get(),))

    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        messagebox.showinfo("Login", "Sucesso!") 
        root.destroy()  # fecha login
        import principal
    else:
        messagebox.showerror("Login", "E-mail ou senha inválidos!")
    
root.configure(bg="#e8f0f6")       

tk.Label(root, text="Login", font=("Segoe UI", 20, "bold"),bg="#e8f0f6").grid(row=1, column=1, columnspan=3, pady=20)

tk.Label(root, text="E-mail",bg="#e8f0f6").grid(row=2, column=1, columnspan=3, pady=15)

email = tk.Entry(root)
email.grid(row=3, column=1, columnspan=3)

tk.Label(root, text="Senha",bg="#e8f0f6").grid(row=4, column=1, columnspan=3, pady=15)

senha = tk.Entry(root, show="*")
senha.grid(row=5, column=1, columnspan=3)

tk.Button(root, text="Entrar", command=validar_login,bg="#4CAF50",
        fg="white",
        activebackground="#45a049",
        bd=0,
        width=10,
        height=1).grid(row=6, column=1, columnspan=3, pady=15)


root.mainloop()