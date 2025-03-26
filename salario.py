
salario=float(input("Digite o valor do salário atual: R$ "))


percentualaumento=float(input("Digite a porcentagem de aumento (%): "))
valoraumento=salario*(percentualaumento / 100)

novosalario=salario+valoraumento

print(f"Valor do aumento: R$ {valoraumento:.2f}")
print(f"Novo salário: R$ {novosalario:.2f}")
