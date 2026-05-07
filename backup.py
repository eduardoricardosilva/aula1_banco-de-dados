import sqlite3

def realizar_backup(db_origem, db_destino):
    try:
        # Conecta ao banco de dados principal (origem)
        conn_origem = sqlite3.connect(db_origem)
        # Conecta (ou cria) o arquivo de backup (destino)
        conn_destino = sqlite3.connect(db_destino)

        # Executa o backup
        with conn_destino:
            conn_origem.backup(conn_destino)
        print(f"Backup concluído com sucesso em: {db_destino}")

    except sqlite3.Error as e:
        print(f"Erro ao realizar backup: {e}")
    finally:
        conn_origem.close()
        conn_destino.close()