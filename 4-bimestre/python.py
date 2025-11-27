#Uso do return - Sem ele não há a soma do item a e b#
def soma(a,b):
    resultado = a + b
    return resultado

x = soma(5,5)
print("o resultado é igual a ",x)

print("+==================================================================================+")

#Uso básico das funções
def OI(professor, turma):
    print(f"O professor {professor} dará aula de funções para a turma {turma}")

OI(professor= "João", turma= "Infoweb 1V")

print("+==================================================================================+")

#Adicionar um valor padrão na função
def alunos(nome= "Maluco1", idade= "Não referido"):
    print(f"O aluno {nome} possui {idade} anos de idade")

alunos()

print("+==================================================================================+")

#teste 1 - adicionar tudo na mesma lista
def adicionar_item(item, lista = []):
    lista.append(item)
    print(lista)
adicionar_item("oi-l1")

print("+==================================================================================+")

#teste 2 - criar uma lista para cada
def adicionar_item(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    print(lista)

adicionar_item("oi-l2")

print("+==================================================================================+")

#Variável global dentro e fora da função
doce_de_verdade = "pudim","caramelo","beterraba"
def doces():
    Doces = "brigadeiro","Doce de leite", "Cuscuz"
    global doce_de_verdade       #Para acessar a variavel global dentro da função é necessário usar "global"
    return print(doce_de_verdade)

doces()
print(Doces)                     #Não é possível acessar uma variável criada dentro de uma função fora dela
print(doce_de_verdade)