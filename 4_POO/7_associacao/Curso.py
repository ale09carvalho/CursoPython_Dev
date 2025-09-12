class Curso:
    def __init__(self, nome_curso):
        #atributos
        self.__nome_curso = nome_curso
        # criar uma lista dentro do construto - atributo da classe
        self.alunos_inscritos = [] # atributo

    # gett e sett
    @property
    def nome_curso(self):
        return self.__nome_curso
    
    @nome_curso.setter
    def nome_curso(self, nome_curso):
        self.__nome_curso = nome_curso

    # metodo de Ação adcionar e listar alunos
    def adicionar_alunos(self, aluno):
        if aluno not in self.alunos_inscritos:
            # referencia a um metodo da classe Aluno
            self.alunos_inscritos.append(aluno) 
            aluno.inscrever_curso(self)  # Associa o curso ao aluno
         
    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_inscritos:
            lista.append(aluno.nome_aluno)
        return lista 
    
