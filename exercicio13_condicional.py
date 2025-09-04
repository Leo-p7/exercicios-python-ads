"""
Ler um número e exibir mensagens dependendo do intervalo
"""
n = int(input("Digite um número: "))
if n <= 10:
    print("mensagem 1")
elif n > 10 and n <= 100:
    print("mensagem 2")
elif n > 100:
    print("mensagem 3")