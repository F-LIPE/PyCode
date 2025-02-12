#nome = "Felipe"
#print("Hello, %s!!!" %nome)

#nome = "Manuel"
#idade = 25
#altura = 1.75
#peso = 70.5
#print(f"Nome: {nome}, Idade: {idade}, Altura: #{altura:.2f}, Peso: {peso:.1f} kg")

#A = 7
#B = 5
#print(A + B * A)
#print("\n")
#print(A + B, 'Hellow'," " ,0)
#print(int())

##aqui comeca LISTA

#A = [1, "oi", 1.01, False]
#print(A[:])

#ista1 = [1, 2]
#lista2 = [3, 4]
#lista3 = [5, 6]
#
#resultado = []
#
#for i in range(len(lista1)):
#  resultado.append(lista1[i] + lista2[i])
#
#print(resultado)

##aqui comeca FOR

#A = int(input("Digite um numero: "))
#B = 0
#for i in range(1, A + 1):
#  B += i
#  print(i, end=" ")
#
#print()
#print("A soma e: ",B)

A = "ABCDEFGHIJKLMNOPQRSTUVRSTUVWXYZ"
alfabeto_com_numeros = {A[i]: i + 1 for i in range(26)}  #dicionario

entrada = input("Digite uma string: ").upper()  #converter para maiuscula

cripty = []  #lista para amazenar os numeros coorespondentes

for letra in entrada:
  if letra in alfabeto_com_numeros:
    cripty.append(str(alfabeto_com_numeros[letra]))

print(' '.join(cripty))
