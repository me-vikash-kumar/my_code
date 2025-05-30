sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'veggie', 'turkey', 'pastrami','mushroom','salmon' ]

finished_sandwich =[]

while 'pastrami' in sandwich_orders :
    print('='*40)
    print ('deli has run out of pastrami')
    print('='*40)
    sandwich_orders.remove('pastrami')

for item in sandwich_orders :
    finished_sandwich.append(item)
    print(f'\n I made your {item} sandwich.')

    print(finished_sandwich)
