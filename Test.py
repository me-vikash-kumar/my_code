def describe_city(city, country='India'):
    print(f'{city} is situated in {country}')

def get_user_input():
    while True:
        city = input("Enter city name: ").strip()
        if city:
            break
        print("City name cannot be empty. Please try again.")
    
    country = input("Enter country name (press Enter for India): ").strip()
    if not country:
        country = 'India'
    
    return city, country

# Get input and call function
a, b = get_user_input()
describe_city(a, b)