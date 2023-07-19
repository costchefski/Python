my_pizzas = ['supreme', 'spicy supreme', 'cheeseburger']
your_pizzas = my_pizzas[:]

my_pizzas.append('volcano')
your_pizzas.append('hawaii')

print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favourite pizzas are:")
for pizza in your_pizzas:
    print(pizza)
