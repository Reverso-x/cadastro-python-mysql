#codigo do sistema.
#Para salvar os dados no seu banco, mude o user e password pelos seu dados.
#Line 23 e Line 24

import mysql.connector

def login():
    print("==== LOGIN ====")
    email = input("Digite seu E-mail: ")
    senha = input("Digite sua Senha: ")
    print(  )
    print("LOGIN COM SUCESSO")
    print(  )
    exit()


def cadastro():
    print("==== CADASTRO ====")
    email = input("Digite seu E-mail: ")
    senha = input("Crie sua Senha: ")
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUA SENHA AQUI",
    database="cadastro_db"
)
    cursor = conexao.cursor()
    sql = "INSERT INTO cadastros_clientes (email, senha) VALUES (%s, %s)"
    valores = (email, senha)
    cursor.execute(sql, valores)
    conexao.commit()
    print(  )
    print("CADASTRADO COM SUCESSO")
    print(  )
    login()


while True:
    print(  )
    print("======== SISTEMA DE CADASTRO E LOGIN ========")
    opcao = input(
        "O que deseja fazer?\n"
        "[1] - Login\n"
        "[2] - Cadastro\n"
        "[3] - Sair\n"
        "Digite: "
    )
    print(  )

    if opcao == "1":
        login()

    elif opcao == "2":
        cadastro()

    elif opcao == "3":
        break

    else:
        print("Opção inválida!")