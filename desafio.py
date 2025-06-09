nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
porc_bonus = float(input("Digite a porcentagem do bonus: "))
bonus = 1000 + salario *porc_bonus
print(f"O valor do seu bonus é {bonus}")
