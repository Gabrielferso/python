class Aluno:  
    def __init__(self, nota):   
        self._nota = nota  
    @property  
    def nota(self):  
        return self._nota  
    @nota.setter  
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        
aluno1 = Aluno(8)
print(aluno1.nota)
aluno1.nota = 9
print(aluno1.nota)  
aluno1.nota = 11 

