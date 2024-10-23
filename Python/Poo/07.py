"""Modele uma classe Aluno com atributos de nome, matrícula e notas em várias disciplinas, e
métodos para calcular a média."""

class Aluno:
    def __init__(self, nome, matricula, disciplinas):
        self.nome = nome
        self.matricula = matricula
        self.disciplinas = disciplinas

    def calculoMedia(self):
        totalNotas = sum(self.disciplinas.values())
        media = totalNotas / len(self.disciplinas)
        print(f"""
        Aluno:      {self.nome} 
        Matricula:  {self.matricula}
        Nota:       {self.disciplinas}
        Media:      {media:.2f}
        """)

nome = input("Digite seu nome: ")
matricula = int(input("Digite sua matricula: "))

disciplinas = {}
resp = ""

while True:
    if resp == "nao".lower() or resp == "não".lower():
        break
    else:
        materia = input("Digite o nome da materia: ")
        notaMateria = float(input("Digite a nota da materia: "))
        
    resp = input("Deseja adicionar mais materias: SIM (para continuar) - NÃO (para encerrar)")
    disciplinas[materia] = notaMateria

aluno1 = Aluno(nome, matricula, disciplinas)

Aluno.calculoMedia(aluno1)
