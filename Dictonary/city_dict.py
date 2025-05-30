paris ={'city':'Paris','country':'France','population':'2.2 million','fact':'Paris is the capital city of France.'}

tokyo ={'city':'Tokyo','country':'Japan','population':'9.5 million','fact':'Tokyo is the capital city of Japan.'}

rome ={'city':'Rome','country':'Italy','population':'2.5 million','fact':'Rome is the capital city of Italy.'}

cities =[paris,tokyo,rome]

for city in cities:
    print(f'\n{city["city"].title()} city is in {city["country"].title()} and has a population of {city["population"]} and a fact about it is {city["fact"]}')