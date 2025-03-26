
preco = float(input("Digite o preço da mercadoria: R$ "))


desconto = float(input("Digite o percentual de desconto (%): "))


desconto = preco * (desconto / 100)

precofinal = preco -desconto

print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Preço a pagar: R$ {precofinal:.2f}")
