def converter(numero):
    numero1 = str(numero)
    reverso = numero1[::-1]
    conversao = int(reverso)
    return(f'Valor ao contrário é: {reverso}')

numero = int(input('Digite um número  inteiro aleatório: '))
c = converter(numero)
print(c)
