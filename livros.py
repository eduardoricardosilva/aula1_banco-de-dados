import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

from categoria import abrir_cadastro

# --- BANCO DE DADOS ---
def conectar():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    return conn

def obter_categorias():
    """Retorna uma lista de tuplas (id, nome) das categorias."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM genero")
    dados = cursor.fetchall()
    conn.close()
    return dados

def obter_autor():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM autor")
    dados = cursor.fetchall()
    conn.close()
    return dados

# --- LÓGICA DAS TELAS ---

def abrir_cadastro_livro(parent, id=None):
    janela_cad = tk.Toplevel(parent)
    janela_cad.title("Editar Categoria" if id else "Cadastrar Livro")
    janela_cad.geometry("350x350")
    
    tk.Label(janela_cad, text="Nome do Livro:", font=("Arial", 10)).pack(pady=10)
    ent_nome = tk.Entry(janela_cad, width=30)
    ent_nome.pack(pady=5)

    def obter_id_selecionado():
            nome_selecionado = combo_categoria.get()
            if nome_selecionado:
                # Buscamos o ID no dicionário usando o nome que está no combo
                id_final = mapeamento_categorias[nome_selecionado]
                return id_final
            return None

    # Se for EDIÇÃO, preenche o campo com o nome atual
    if id:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT nome_genero FROM categoria WHERE id_categoria = ?", (id))
        resultado = cursor.fetchone()
        if resultado:
            ent_nome.insert(0, resultado[0])
        conn.close()
    
    def salvar():
        nome = ent_nome.get()
        if not nome.strip():
            messagebox.showwarning("Aviso", "O nome não pode estar vazio.")
            return

        conn = conectar()
        cursor = conn.cursor()
        
        if id:
            # Lógica de Atualização
            cursor.execute("UPDATE genero SET nome = ? WHERE id_genero = ?", (nome, id))
            mensagem = "Categoria atualizada com sucesso!"
        else:
            # Lógica de Inserção
            id_para_sql = obter_id_selecionado()
            cursor.execute("INSERT INTO livros (titulo,id_genero) VALUES (?)", (nome,id_para_sql))
            mensagem = "Categoria cadastrada com sucesso!"
            
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", mensagem)
        janela_cad.destroy()

    btn_texto = "Atualizar" if id else "Salvar"
    btn_cor = "#ffcc00" if id else "lightgreen"


            # Campo: Seleção de Categoria (Combobox)
    tk.Label(janela_cad, text="Selecione a Categoria:").pack(pady=(15, 5))
    
        # Buscamos as categorias do banco
    lista_categorias = obter_categorias() # Formato: [(1, 'Eletrônicos'), (2, 'Móveis')]

    mapeamento_categorias = {nome_categoria: id_categoria for id_categoria, nome_categoria in lista_categorias}
    nomes_categorias = list(mapeamento_categorias.keys())
    
        # Criamos uma lista apenas com os nomes para exibir no Combobox
    nomes_categorias = [c[1] for c in lista_categorias]
    
    combo_categoria = ttk.Combobox(janela_cad, values=nomes_categorias, width=32, state="readonly")
    combo_categoria.pack()

        #Campo: seleção do autor#

    tk.Label(janela_cad, text="Selecione o autor:").pack(pady=(15, 5))
    
        # Buscamos autores do banco
    lista_categorias = obter_categorias() # Formato: [(1, 'Eletrônicos'), (2, 'Móveis')]

    mapeamento_categorias = {nome_categoria: id_categoria for id_categoria, nome_categoria in lista_categorias}
    nomes_categorias = list(mapeamento_categorias.keys())
    
        # Criamos uma lista apenas com os nomes para exibir no Combobox
    nomes_categorias = [c[1] for c in lista_categorias]
    
    combo_categoria = ttk.Combobox(janela_cad, values=nomes_categorias, width=32, state="readonly")
    combo_categoria.pack()

    tk.Button(janela_cad, text=btn_texto, command=salvar, bg=btn_cor).pack(pady=20)

def abrir_consulta(parent):
    janela_con = tk.Toplevel(parent)
    janela_con.title("Consultar genero")
    janela_con.geometry("500x500") 

    # 1. Tabela (Treeview)
    colunas = ("ID", "Titulo")
    tabela = ttk.Treeview(janela_con, columns=colunas, show="headings")
    tabela.heading("ID", text="ID")
    tabela.heading("Nome da Categoria", text="Nome da Categoria")
    tabela.column("ID", width=50, anchor="center")
    tabela.pack(pady=20, padx=10, fill="both", expand=True)

    # 2. Função interna para o botão Editar
    def executar_edicao():
        item_selecionado = tabela.selection()
        
        if not item_selecionado:
            messagebox.showwarning("Aviso", "Por favor, selecione uma categoria na lista!")
            return

        valores = tabela.item(item_selecionado, "values")
        id_cat = valores[0]

        # Abre a mesma tela de cadastro, mas agora enviando o ID para modo edição
        abrir_cadastro(parent, id=id_cat)
        janela_con.destroy() 

    # 3. Botões de Ação
    frame_botoes = tk.Frame(janela_con)
    frame_botoes.pack(pady=10)

    btn_editar = tk.Button(
        frame_botoes, 
        text="Editar Selecionada", 
        command=executar_edicao,
        bg="#ffcc00",
        font=("Arial", 10, "bold"),
        width=20
    )
    btn_editar.pack(side="left", padx=5)

    # 4. Buscar dados iniciais
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM genero")
    for linha in cursor.fetchall():
        tabela.insert("", tk.END, values=linha)
    conn.close()

