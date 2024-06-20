# Lê a quantia em reais
quantia = int(input())

# Calcula a quantidade de cada nota necessária
notas100 = quantia // 100
quantia %= 100

notas50 = quantia // 50
quantia %= 50

notas20 = quantia // 20
quantia %= 20

notas10 = quantia // 10
quantia %= 10

notas5 = quantia // 5
quantia %= 5

notas2 = quantia // 2
quantia %= 2

notas1 = quantia // 1

# Imprime o resultado formatado
print(f"{notas100} nota(s) de R$100,00")
print(f"{notas50} nota(s) de R$50,00")
print(f"{notas20} nota(s) de R$20,00")
print(f"{notas10} nota(s) de R$10,00")
print(f"{notas5} nota(s) de R$5,00")
print(f"{notas2} nota(s) de R$2,00")
print(f"{notas1} nota(s) de R$1,00")