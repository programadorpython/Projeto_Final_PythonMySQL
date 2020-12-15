import mysql.connector


def conectar_db(host, usuario, senha, nome_db=None):
    """
    Criar objeto de conexão com o banco MySQL
    :param host: string
    :param usuario: string
    :param senha: string
    :param nome_db: string
    :return: object meu_db
    """
    if not nome_db:
        meu_db = mysql.connector.connect(
            host=host,
            user=usuario,
            passwd=senha
        )
    else:
        meu_db = mysql.connector.connect(
            host=host,
            user=usuario,
            passwd=senha,
            database=nome_db
        )
    return meu_db
