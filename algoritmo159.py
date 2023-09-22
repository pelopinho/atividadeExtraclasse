import math
x = float(input("\n Digite o valor de x: "))

if x > 4 or x < -4:
    fx = (5* x + 3) / math.sqrt(x**2 - 16)
    print("\n f(x) = ",fx)
else:
    print("\n Não pode ser feita!")

print("\n")