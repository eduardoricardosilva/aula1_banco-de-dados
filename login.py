import tkinter as tk
from tkinter import messagebox

def montar_tela_login(container, comando_entrar):
    # Usamos o container (root) enviado pelo main, não criamos um novo tk.Tk()
    container.title("Tela de Login")
    container.geometry("400x400")
    container.configure(bg="#e8f0f6")

    # Limpa o container antes de montar
    for widget in container.winfo_children():
        widget.destroy()

    tk.Label(container, text="Login", font=("Segoe UI", 25, "bold"), bg="#e8f0f6").pack(pady=20)

    tk.Label(container, text="E-mail", font=("Segoe UI", 10), bg="#e8f0f6").pack(pady=5)
    ent_email = tk.Entry(container, width=25, font=("Segoe UI", 12))
    ent_email.pack(pady=5)

    tk.Label(container, text="Senha", font=("Segoe UI", 10), bg="#e8f0f6").pack(pady=5)
    ent_senha = tk.Entry(container, show="*", width=25, font=("Segoe UI", 12))
    ent_senha.pack(pady=5)

    # A mágica acontece aqui: pegamos o .get() apenas quando o botão é clicado
    btn = tk.Button(
        container, 
        text="Entrar", 
        command=lambda: comando_entrar(ent_email.get(), ent_senha.get()),
        bg="#4CAF50",
        fg="black",
        font=("Segoe UI", 11, "bold"),
        activebackground="#45a049",
        activeforeground="white",
        width=10,
        height=1,
        cursor="hand2",
        relief="flat",
        bd=0
    )
    btn.pack(pady=20)