"""22. Cadastro de Alunos - Abstração, Encapsulamento:
Crie uma classe para representar um aluno, com atributos como nome, matrícula e notas. Utilize 
abstração para definir métodos como calcular_media e encapsulamento para proteger os dados das 
notas.
"""

class Aluno:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.__notas = [nota1, nota2, nota3]
    
    def calcular_media(self):
        media = sum(self.__notas)/3

        if media < 6:
            print(f"reprovado, media: {media}")
        else:
            print(f"aprovado, media: {media}")

nome = input("nome do aluno: ")
matricula = int(input("matricula do aluno: "))
nota1 = float(input("1° nota do aluno: "))
nota2 = float(input("2° nota do aluno: "))
nota3 = float(input("3° nota do aluno: "))

aluno1 = Aluno(nome, matricula, [nota1, nota2, nota3])

aluno1.calcular_media()


