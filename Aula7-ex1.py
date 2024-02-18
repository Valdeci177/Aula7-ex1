class GerenciadorAlunos:
    def __init__(self):
        self.alunos = {}

    def AdicionarAluno(self):
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite o número de matrícula do aluno: ")
        self.alunos[matricula] = nome
        print("Aluno adicionado com sucesso!")

    def RemoverAluno(self):
        matricula = input("Digite o número de matrícula do aluno a ser removido: ")
        if matricula in self.alunos:
            del self.alunos[matricula]
            print("Aluno removido com sucesso!")
        else:
            print("Matrícula não encontrada.")

    def AtualizarAluno(self):
        matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
        if matricula in self.alunos:
            nome = input("Digite o novo nome do aluno: ")
            self.alunos[matricula] = nome
            print("Nome do aluno atualizado com sucesso!")
        else:
            print("Matrícula não encontrada.")

    def VerAlunos(self):
        print("Lista de Alunos:")
        for matricula, nome in self.alunos.items():
            print("Matrícula:", matricula, "- Nome:", nome)


# Testando o módulo
if __name__ == "__main__":
    gerenciador = GerenciadorAlunos()
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Atualizar aluno")
        print("4. Ver alunos")
        print("5. Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            gerenciador.AdicionarAluno()
        elif opcao == "2":
            gerenciador.RemoverAluno()
        elif opcao == "3":
            gerenciador.AtualizarAluno()
        elif opcao == "4":
            gerenciador.VerAlunos()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")