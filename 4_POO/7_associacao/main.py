# ASSOCIAÇAO, as classes possuem relação entre si, mas podem existir de forma independente uma da outra.
import Curso
import Aluno

# instacia as classes
def main():
    # instancia dos cursos - obj
    curso1 = Curso.Curso(nome_curso="Python")
    curso2 = Curso.Curso(nome_curso="Java")
    curso3 = Curso.Curso(nome_curso="PHP")
    # instancia dos alunos - obj
    aluno1 = Aluno.Aluno(nome_aluno="Fulano", matricula="1")
    aluno2 = Aluno.Aluno(nome_aluno="Sicrano", matricula="2")
    aluno3 = Aluno.Aluno(nome_aluno="Beltrano", matricula="3")
    aluno4 = Aluno.Aluno(nome_aluno="João", matricula="4")
    aluno5 = Aluno.Aluno(nome_aluno="Maria", matricula="5")
    aluno6 = Aluno.Aluno(nome_aluno="Jose", matricula="6")
    aluno7 = Aluno.Aluno(nome_aluno="Jorge", matricula="7")

    # inscrevendo os alunos no curso 1
    aluno1.inscrever_curso(curso1)
    aluno2.inscrever_curso(curso1)
    aluno3.inscrever_curso(curso1)
    aluno4.inscrever_curso(curso1)

    # inscrevendo os alunos no curso 2
    aluno5.inscrever_curso(curso2)
    aluno6.inscrever_curso(curso2)

    curso3.adicionar_alunos(aluno7)

    # Lista de Alunos do Curso - saída de dados
    print(f"Curso: {curso1.nome_curso}")
    
    for aluno in curso1.listar_alunos():
        print(aluno)
          
if __name__ == "__main__":
    main()
