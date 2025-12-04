n = 5
while True:
    if n < 1:
        break
    print(n)
    n -= 1
print("Decolar!")

#---------------------------------------------------------------------------------#

def contagem(n):
    if n < 1:
        print("Decolar!")
    else:
        print(f"Aqui é a função: {n}")
        contagem(n - 1)
    
contagem(5)

#---------------------------------------------------------------------------------#

def fatorial(x):
    if x > 0:
        return x * fatorial(x-1)
    else:
        return 1

print(fatorial(5))

#---------------------------------------------------------------------------------#

def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(7))

#------------------------------- FUNÇÃO LAMBDA -----------------------------------#
                                
n = int(input())
dobrar = lambda n: n * 2
print(dobrar(n))

#------------------------------- FUNÇÃO LAMBDA -----------------------------------#

def aplicar_op(a, b, op):
    return op(a,b)
resultado = aplicar_op(2,3, lambda x, y: x * y)