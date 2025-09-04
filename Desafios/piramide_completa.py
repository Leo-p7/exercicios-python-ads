"""
Desafio: Pirâmide completa
Lê um número N e imprime uma pirâmide simétrica com blocos (#).
"""
n = int(input("Digite o tamanho da piramide: "))
for i in range (1,n+1):
    blocos = "#"*i
    espacos = " "* (n-i)
    direito = "#"*(i-1)
    print(espacos + blocos + direito)
