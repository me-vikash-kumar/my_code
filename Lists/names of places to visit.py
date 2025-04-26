list_of_places = ['hydrabad','kashmir','some mountainous place','a calm place','nice beach']

print(list_of_places)

print(sorted(list_of_places))

print(sorted(list_of_places,reverse=True ))

print(f'original list {list_of_places}')

list_of_places.reverse()

print(f"reversed list of places {list_of_places}")

list_of_places.reverse()

print(f'original list {list_of_places}')

list_of_places.sort()

print(f'order of list has permanently changes {list_of_places}')

list_of_places.sort(reverse=True)

print(f'new list in reversed order list has changed permanently again{list_of_places}')
