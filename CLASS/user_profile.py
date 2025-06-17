def user_profile(first_name,last_name,**items):
    items['first name']=first_name
    items['last name']=last_name
    return items

me_name=user_profile('ravi','kumar',age=21,city='delhi')

print(me_name)