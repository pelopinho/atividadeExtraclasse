op = int(input("\nDigite:\n1 - Região Norte\n2 - Região Nordeste\n3 - Região Centro-Oeste\n4 - Região Sul\n"))
iv = int(input("\n Digite:\n1 - Ida\n2 - Ida e Volta\n"))

if(op == 1):
    if(iv == 1):
        print("\nO valor da passagem de ida para a R. Norte é R$ 500,00")
    else:
        print("\nO valor da passagem de ida e volta para R. Norte é R$ 950,00")
elif(op == 2): 
    if(iv == 1):
        print("\nO valor da passagem de ida para a R. Nordeste é R$ 350,00")
    else:
        print("\nO valor da passagem de ida e volta para a R. Nordeste é R$ 650,00")
elif(op == 3): 
    if(iv == 1):
        print("\nO valor da passagem de ida para a R. Centro-Oeste é R$ 350,00")
    else:
        print("\nO valor da passagem de ida e volta para a R. Centro-Oeste é R$ 600,00")
elif(op == 4): 
    if(iv == 1):
        print("\nO valor da passagem de ida para a R. Sul é R$ 300,00")
    else:
        print("\nO valor da passagem de ida e volta para a R. Sul é R$ 500,00")

else:
    print("\nOpção inexistente")

print("\n")
