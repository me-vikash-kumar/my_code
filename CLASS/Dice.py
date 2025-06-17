import random
class Dice:
    def __init__(self,sides=6):
        self.sides=sides
    
    def roll_die(self):
        value=random.randrange(1,self.sides+1)
        print(f'{value}')


if __name__=='__main__':
        ludo=Dice()

        ludo.roll_die()
        ludo.roll_die()
        ludo.roll_die()
        ludo.roll_die()
        ludo.roll_die()
        ludo.roll_die()
        ludo.roll_die()
        ludo.roll_die()

        print('='*90)

        ten_face_ludo=Dice(10)

        ten_face_ludo.roll_die()
        ten_face_ludo.roll_die()
        ten_face_ludo.roll_die()
        ten_face_ludo.roll_die()