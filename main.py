from helpers import conectar_db
from configurar_db import HOST, USER, PASSWORD, DATABASE_NAME

meu_db = conectar_db(HOST, USER, PASSWORD, DATABASE_NAME)
meu_cursor = meu_db.cursor()

while True:
    mensagem = "Qual a opção desejada: (1-Inserir, 2-Visualizar, 3-Sair): "
    inicial = input(mensagem)

    if inicial == "3":
        break
    elif inicial == "2":
        meu_cursor.execute("SELECT * FROM receita_despesa")
        resultado = meu_cursor.fetchall()

        print()
        print("{: >10} {: >10} {: >20} {: >10}".format("DATA", "TIPO", "DESCRIÇÃO", "VALOR"))
        soma_entradas = 0
        soma_despesas = 0

        for linha in resultado:
            print("{: >10} {: >10} {: >20} R${: >10}".format(str(linha[0]), linha[1], linha[2], linha[3]))
            if linha[1] == "Entrada":
                soma_entradas += linha[3]
            else:
                soma_despesas += linha[3]

        print()
        print(f"Total Entradas: R$ {soma_entradas: >10}")
        print(f"Total Despesas: R$ {soma_despesas: >10}")
        print(f"Saldo Final: R$ {soma_entradas - soma_despesas: >10}")
    else:
        data = input("Insira data no formato AAAA-MM-DD: ")
        tipo = input("Qual o tipo (1-Entrada, 2-Despesa): ")
        tipo = "Entrada" if tipo == "1" else "Despesa"
        descricao = input("Descrição breve do registro: ")
        valor = input("Qual o valor do registro: ")

        insert_query = "INSERT INTO receita_despesa (data, tipo, descricao, valor) VALUES (%s, %s, %s, %s)"
        registro = (data, tipo, descricao, valor)
        meu_cursor.execute(insert_query, registro)
        meu_db.commit()
