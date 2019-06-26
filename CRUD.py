# Imports dos pacotes
import sqlite3
import random


#Criando conexao com o banco de dados
SQLConnection = sqlite3.connect("CRUD.db")
cursor = SQLConnection.cursor()


#criando tabela
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS estudantes(matricula PRIMARY KEY NOT NULL, name VARCHAR(50), age INTEGER, nota1 REAL, nota2 REAL, nota3 REAL)")


def insert_data(name, age, nota1, nota2, nota3):
    new_name = name
    new_age = age
    new_matricula = random.randrange(1, 100)
    nota1 = nota1
    nota2 = nota2
    nota3 = nota3

    cursor.execute("INSERT INTO estudantes(name, age, matricula, nota1, nota2, nota3) VALUES(?, ?, ?, ?, ?, ?)", (new_name, new_age, new_matricula, nota1, nota2, nota3))
    SQLConnection.commit()

# Ler registros
def read_data():
    cursor.execute("SELECT * FROM estudantes")

    for estudante in cursor.fetchall():
        print(estudante)


def data_consulting(key):
    key = key
    search = cursor.execute("SELECT * FROM estudantes WHERE matricula = %d" % key)
    search = str(search)
    print(search)
    SQLConnection.commit()


def delete_data(key):
    key = key
    cursor.execute("DELETE FROM estudantes WHERE matricula = %d" % key)
    SQLConnection.commit()

class Aluno():

    def __init__(self, name, age, nota1, nota2, nota3):
        self._name = name
        self._age = age
        self._nota1 = nota1
        self._nota2 = nota2
        self._nota3 = nota3

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, _age):
        self._age = age

    @property
    def nota1(self):
        return self._nota1

    @nota1.setter
    def nota1(self, nota1):
        self._nota1 = nota1

    @property
    def nota2(self):
        return self._nota2

    @nota2.setter
    def nota2(self, nota2):
        self._nota2 = nota2

    @property
    def nota3(self):
        return self._nota3

    @nota3.setter
    def nota3(self, nota3):
        self._nota3 = nota3



opcao = ""

while opcao != 5:


    print("\n------SISTEMA ESCOLAR DE CADASTRO------")
    print("\n1 - Cadastrar Estudante \n2 - Excluir registro "
          "\n3 - Mostrar Registros \n4 - Consultar Registro\n5 - SAIR")

    opcao = int(input("\nSelecione uma opção: "))

    if opcao == 1:
        try:
            print("\n----CADASTRO DE ESTUDANTE----")
            name = input("\nEntre com o nome do aluno para cadastro: ")
            age = int(input("Entre com a idade do aluno: "))
            nota1 = float(input("Entre com a primeira nota do aluno: "))
            nota2 = float(input("Entre com a segunda nota do aluno: "))
            nota3 = float(input("Entre com a terceira nota do aluno: "))
            aluno = Aluno(name, age, nota1, nota2, nota3)
            create_table()
            insert_data(aluno.name, aluno.age, aluno.nota1, aluno.nota2, aluno.nota3)
            print("Ragistro adicionado com sucesso.")

        except ValueError:
            print("Entrada de dados inválida esperado um valor numerico inteiro")
            break

    elif opcao == 2:
        try:
            print("\n---DELETAR REGISTRO---\n")
            key = int(input("Entre com a matricula do aluno a ser deletado: "))
            delete_data(key)
            print("Registro excluido com sucesso.")

        except ValueError:
            print("Entrada de dados inválida esperado um valor numerico inteiro")
            break

    elif opcao == 3:
        print("\n---MOSTRANDO REGISTROS---\n")
        read_data()

    elif opcao == 4:
        try:
            print("\n---CONSULTANDO REGISTROS---\n")
            key = int(input("Entre com a matricula do aluno para busca: "))
            data_consulting(key)

        except ValueError:
            print("Entrada de dados inválida esperado um valor numerico inteiro")
            break

    elif opcao == 5:
        break