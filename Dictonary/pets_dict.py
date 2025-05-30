rara ={"animal": "cat",'owner': 'Mary','age': '5','gender': 'Female','color': 'white'}

jessi ={"animal": "dog",'owner': 'Jessica','age': '2','gender': 'Female','color': 'black'}

luna ={"animal": "rabbit",'owner': 'Luna','age': '1','gender': 'Female','color': 'red'}

gloria ={'animal':'lynx','owner': 'Dori','age': '3','gender': 'Female','color': 'white'}

pets=[rara,jessi,luna,gloria]

for pet in pets:
    
    print(f"\n{pet['owner']} has a pet {pet['animal']} that is {pet['color']} {pet['gender']} and is {pet['age']} year old.")


