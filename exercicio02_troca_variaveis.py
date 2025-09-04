"""
Ler dois números e trocar os valores entre si (vA <-> vB)
"""
vA = float(input("Digite o primeiro número: "))
vB = float(input("Digite o segundo número: "))
print("Antes da troca: vA =", vA, "vB =", vB)
vA, vB = vB, vA
print("Depois da troca: vA =", vA, "vB =", vB)
