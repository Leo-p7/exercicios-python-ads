"""
Desafio: Pirâmide alinhada à esquerda
Lê um número N e imprime uma pirâmide com blocos (#) alinhada à esquerda.
"""
n = int(input("Digite o tamanho da piramide: "))
for i in range (1,n+1):
    blocos = "#"*i
    espacos = " "* (n+i)
    print(blocos + espacos)