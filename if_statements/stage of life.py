while True:
    try:
        age = input("Enter anyhting else to quit.\nEnter your age: ")
        age = int(age)
        if age <= 2 :
            print(f'You are a baby.\n')
        elif age >=2  and age <= 4:
            print(f'You are a toddler.\n')
        elif age >=4  and age <= 13:
            print(f'You are a kid.\n')
        elif age >=13  and age <= 20:
            print(f'You are a teenager.\n')
        elif age >=20  and age <= 65:
            print(f'You are an adult.\n')
        else:
            print(f'You are an elder.\n')
    except ValueError:
        print("Thanks for using this program.")
        break
