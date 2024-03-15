nota1 = (float(input("Digite a sua nota: ")))
nota2 = (float(input("Digite a sua segunda nota: ")))

media = (nota1 + nota2) / 2
print(f'Sua média foi {media:.2f}')

if media >= 5 and media < 7:
    print("Você está de recuperação")
elif media >= 7:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")