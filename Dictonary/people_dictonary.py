ravi={'first_name':'ravi','last_name':'kumar','age':21,'city':'delhi'}

james={'first_name':'james','last_name':'bond','age':29,'city':'london'}

tommy={'first_name':'tommy','last_name':'cruise','age':25,'city':'new york'}

naresh={'first_name':'naresh','last_name':'kumar','age':27,'city':'mumbai'}

people=[ravi,james,tommy,naresh]

for person in people:
    print(f'His first name is {person["first_name"].title()} and last name is {person["last_name"].title()} and he is {person["age"]} years old and he lives in {person["city"].title()}.\n')

