import random

class lucky_draw:
    
    def __init__(self):
        self.lucky_set=[1,2,3,4,5,6,7,8,9,12,'s','h','f','y']
        self.ticket=[]
    
    def lottery(self):
        for i in range(4):
           self.ticket.append(random.choice(self.lucky_set))
        return self.ticket
    
    def lottery_reset(self):
        self.ticket=[]
    
my_ticket=[8,'s',5,'y']
lottery_analysis=lucky_draw()
tikkk=[]
count=0
while True:
    if my_ticket==tikkk:
        break
    else:
        count+=1
        tikkk=lottery_analysis.lottery()
        print(tikkk)
        print(count)
        lottery_analysis.lottery_reset()

print(f'It took this much loops to win :{count}')




