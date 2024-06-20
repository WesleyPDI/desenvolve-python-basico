# Lê o valor da temperatura em graus Fahrenheit
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# Converte a temperatura de Fahrenheit para Celsius
celsius = int((fahrenheit - 32) * (5/9))

# Imprime o resultado formatado
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")