"""
Calcular a média ponderada entre duas notas com seus respectivos pesos
"""
nota1 = float(input("Digite a nota 1: "))
peso1 = float(input("Digite o peso 1: "))
nota2 = float(input("Digite a nota 2: "))
peso2 = float(input("Digite o peso 2: "))

resultado = ((nota1 * peso1) + (nota2 * peso2)) / (peso1 + peso2)
print("A média ponderada é:", resultado)
