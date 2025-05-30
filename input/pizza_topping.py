topping= ""

while True:
    topping = input('\nPlease enter the topping of your choice:')
    
    if topping=='quit':
        break
    print(f'I will add {topping} to your pizza')