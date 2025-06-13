class Restaurant :
    '''Restaurant class'''
    def __init__(self,res_name,cuisine):
        self.res_name = res_name
        self.cuisine = cuisine
        self.number_served=0

    def describe_restaurant(self):
        print(f"{self.res_name} is a {self.cuisine} restaurant.")

    def open_restaurant(self):
        print(f"{self.res_name} is now open!")

    def set_number_served(self,served):
        self.number_served=served

    def increment_number_served(self,increment):
        self.number_served += increment

if __name__ == "__main__":
    gulmohar = Restaurant('Gulmohar','Indian')

    print(gulmohar.res_name)

    print(gulmohar.cuisine)

    gulmohar.describe_restaurant()

    gulmohar.open_restaurant()

    print("="*94)

    wok_tok=Restaurant('wok tok','chinese')

    la_Palette=Restaurant('La Palette','French')

    wok_tok.describe_restaurant()

    la_Palette.describe_restaurant()
    print(la_Palette.number_served)
    la_Palette.set_number_served(12)
    print(la_Palette.number_served)
    la_Palette.increment_number_served(45)
    print(la_Palette.number_served)
