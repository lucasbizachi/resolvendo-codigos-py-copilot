def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "O número {} é par.".format(numero)
    else:
        return "O número {} é ímpar.".format(numero)

# Receber entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Chamar a função para verificar se o número é par ou ímpar
resultado = verificar_par_impar(numero)

# Imprimir o resultado
print(resultado)
