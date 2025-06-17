from Class_Restaurant import Restaurant

class Ice_Cream_Stand(Restaurant):
    '''special case of a restaurant'''
    def __init__(self, res_name,theme, cuisine='Ice Cream'):
        super().__init__(res_name,cuisine)
        self.theme=theme
        self.flavors=['Chocolate', 'Vanilla', 'Strawberry']
    def description(self):
        print(f"{self.res_name} has a {self.theme} theme")
    
    def show_flavors(self):
        print("We have: ")
        for flavor in self.flavors:
            print(flavor)


gardenia=Restaurant('Gardenia','Italian')

space_ice = Ice_Cream_Stand("Galaxy Scoops", "Space Adventure")

space_ice.describe_restaurant()

gulmohar = Restaurant('Gulmohar','Indian')

space_ice.show_flavors()
