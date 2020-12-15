from helpers import conectar_db

DATABASE_NAME = "controle_financeiro"
HOST = "localhost"
USER = "root"
PASSWORD = "senha123456"

# Criar o Banco de Dados
meu_db = conectar_db(HOST, USER, PASSWORD)
meu_cursor = meu_db.cursor()
meu_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}")

# Criar a tabela do banco
meu_db = conectar_db(HOST, USER, PASSWORD, DATABASE_NAME)
meu_cursor = meu_db.cursor()
meu_cursor.execute("CREATE TABLE IF NOT EXISTS receita_despesa "
                   "("
                   "data DATE,"
                   "tipo VARCHAR(255),"
                   "descricao VARCHAR(255),"
                   "valor DECIMAL(10,2),"
                   "id_entrada INTEGER AUTO_INCREMENT PRIMARY KEY"
                   ")")
