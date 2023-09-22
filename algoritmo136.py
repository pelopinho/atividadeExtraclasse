nome = input("\n Entre com o nome: ")
idade = int(input("\n Entre com a idade: "))

if (idade <= 10):
    print("\n",nome,"pagará R$ 30,00")
elif (idade <= 29):
    print("\n",nome,"pagará R$ 60,00")
elif (idade <= 45):
    print("\n",nome,"pagará R$ 120,00")
elif (idade <= 59):
    print("\n",nome,"pagará R$ 150,00")
elif (idade <= 65):
    print("\n",nome,"pagará R$ 250,00")
else:
    print("\n",nome,"pagará R$ 400,00")

print("\n")