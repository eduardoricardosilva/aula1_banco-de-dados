import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import categoria
import livros
import backup
from cadastro_livro import janela_cadastro_livro

# --- FUNÇÃO DA TELA PRINCIPAL ---
def montar_tela_principal(container):
    # 1. Limpeza da tela
    for widget in container.winfo_children():
        widget.destroy()

    container.title("Sistema Interno - Gerenciador de Biblioteca")
    # 2. Barra de Menus
    barra_menu = tk.Menu(container)
    menu_categorias = tk.Menu(barra_menu, tearoff=0)
    menu_categorias.add_command(label="Cadastrar Nova", command=lambda: categoria.abrir_form_categoria(container))
    menu_categorias.add_command(label="Consultar Todas", command=lambda: categoria.abrir_consulta(container))
    menu_categorias.add_separator()
    menu_categorias.add_command(label="Sair", command=container.quit)
    barra_menu.add_cascade(label="Categorias", menu=menu_categorias)
    container.config(menu=barra_menu)

    # 3. Cabeçalho com Data
    data_hoje = datetime.now().strftime("%d/%m/%Y")
    tk.Label(container, text=f"Data: {data_hoje}",bg="#e8f0f6", font=("Arial", 10)).pack(anchor="e", padx=10)
    tk.Label(container, text="Área Restrita", fg="green", font=("Arial", 12, "bold"), bg="#e8f0f6").pack(pady=5)
    tk.Label(container, text="GERENCIADOR BIBLIOTECA", font=("Arial", 14, "bold"),bg="#e8f0f6").pack(pady=20)

    # 4. Botões com nomes únicos
    btn_cons_livros = tk.Button(container, text="CONSULTAR LIVROS", width=25, height=2, 
    command=lambda: livros.abrir_consulta(container), bg="#e1e1e1")
    btn_cons_livros.pack(pady=5)

    btn_novo_cad = tk.Button(container, text="CADASTRAR LIVROS", width=25, height=2, 
    command=lambda: janela_cadastro_livro(container), bg="#e1e1e1")
    btn_novo_cad.pack(pady=5)


    btn_cad_livro = tk.Button(container, text="GERENCIAR USUÁRIOS", width=25, height=2, 
    command=lambda: livros.abrir_cadastro_livro(container), bg="#e1e1e1")
    btn_cad_livro.pack(pady=5)

    btn_bkp = tk.Button(container, text="BACKUP DO SISTEMA", width=25, height=2, 
                        command=lambda: backup.realizar_backup("banco.db", "backup_biblioteca.db"), 
                        bg="#d1e7dd")
    btn_bkp.pack(pady=5)

    btn_sair = tk.Button(container, text="SAIR", width=25, command=container.quit, fg="red")
    btn_sair.pack(pady=20)

# --- EXECUÇÃO DO PROGRAMA ---
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x600") # Aumentei um pouco para caber os botões novos
    # Chamamos a função para desenhar a tela
    montar_tela_principal(root)
    # O mainloop fica aqui, no final de tudo
    root.mainloop()