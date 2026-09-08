produto = input("Digite o nome do produto: ")
mercado1 = input("Digite o nome do 1° mercado: ")
preco1 = float(input(f"o2}"))Digite o valor do mercado {mercado1}:"))
mercado2 = inout("Digite o nome do 2° mercado:")
preco2 = float(input(f"Digite o valor do mercado {mercado2} :"))
mercado3 = input("Digite o nome 3° mercado: ")
preco3 = float(input(f"Digite o valor do mercado {mercado3}: "))

if preco1 < preco2 and preco1 < preco3:
    print(f"O mercado {mercado1} tem o menor preço, que é de R$ {preco1}")
elif preco2 < preco1 and preco2 < preco3:
    print(f"Omercado {mercado2} tem o menor preço, que é de R$ {preco2}")
elif preco3 < preco1 and preco3 < preco2:
    print(f"Omercado {mercado3} tem o menor preço, que é de R$ {preco3}")