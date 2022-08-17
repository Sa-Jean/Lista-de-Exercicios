#Ex 6 - Calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

d = int(input(f'Digite qual a distancia do percuso em KM: '))
v = int(input(f'Digite a velocidade media esperada para a viagem: '))

print(f'O tempo de viagem estimado é de: {d / v: .1f} horas')