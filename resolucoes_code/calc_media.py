def calcular_media(nota1, nota2, nota3):
    # Calcular a média das três notas
    media = (nota1 + nota2 + nota3) / 3
    return media

# Solicitar as três notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Chamar a função para calcular a média das notas fornecidas
media_notas = calcular_media(nota1, nota2, nota3)

# Imprimir a média das notas
print("A média das três notas é:", media_notas)

# Avaliar a média e fornecer uma mensagem de acordo com o resultado
if media_notas < 5:
    print("Você foi reprovado.")
elif media_notas == 6:
    print("Você ficou em recuperação.")
elif media_notas >= 7 and media_notas <= 10:
    print("Parabéns! Você foi aprovado.")
else:
    print("A média está fora do intervalo esperado.")
