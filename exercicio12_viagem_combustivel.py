"""
Calcular litros de gasolina e custo da viagem
Distância = 520 km, Consumo = 12 km/l, Preço = 4,50
"""
distancia = int(input("distancia em km: ")) 
consumo = int(input("Consumo em km/l: "))
litros = distancia / consumo
preço = float(input("Valor do combustível:"))
print("A quantidade de litros de combustível sera:", litros)
print("O custo da viagem com combustível vai ser:", litros * 4.50 )
