def verificar_palindromo(palavra):
    # Remover espaços em branco e converter a palavra para minúsculas
    palavra = palavra.replace(" ", "").lower()
    
    # Inverter a palavra
    palavra_invertida = palavra[::-1]
    
    # Verificar se a palavra original é igual à palavra invertida
    if palavra == palavra_invertida:
        return True
    else:
        return False

# Solicitar uma palavra ao usuário
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

# Chamar a função para verificar se a palavra é um palíndromo
resultado = verificar_palindromo(palavra)

# Imprimir o resultado
if resultado:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
