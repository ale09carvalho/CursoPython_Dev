# Classe Aluno
class Aluno:
    #atributos
    def __init__(self, nome_aluno, matricula):
        self.__nome_aluno = nome_aluno
        self.__matricula = matricula
        # lista dos valores do objto da classe outra classe
        self.cursos_inscritos = []
    
    # getter e Sett
    @property
    def nome_aluno(self):
        return self.__nome_aluno
    
    @nome_aluno.setter
    def nome_aluno(self, nome_aluno):
        self.__nome_aluno = nome_aluno
    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    # ---- metodo de Ação - adcionar e listar alunos-----
    def inscrever_curso(self, curso):
        if curso not in self.cursos_inscritos:
            # referencia a um metodo da classe Curso
            self.cursos_inscritos.append(curso)
            curso.adicionar_alunos(self)  # Associa o aluno ao curso

    def listar_cursos(self):
        lista = []
        for curso in self.cursos_inscritos:
            lista.append(curso.nome_curso)
        return lista

