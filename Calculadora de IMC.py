peso = int(input('¿Cuál es tu peso?(en kg): '))
altura = int(input('¿Cuál es tu altura?(en cm): '))
altura2 = altura / 100
imc = peso / ((altura2) ** 2)
total = round(imc,2)
print('Tu índice de masa corporal es '+str(total))

#incluido
if total >= 18 and total < 25:
    print('Tu IBM está normal')

elif total >= 25:
    print('Tienes sobrepeso (REVISAR)')

elif total < 18:
    print('Tienes bajo peso (REVISAR)')