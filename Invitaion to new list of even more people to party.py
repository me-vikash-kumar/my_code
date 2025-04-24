print('Unfortunately you are allowed to invite only two people')

people_to_invite =['leonardo da vinci','jorden b peterson','jeffrey kaplan','joshua meyer','harold','james bon','jakie chan']



for people in range(len(people_to_invite)-2):
    
     place_holder=people_to_invite.pop()


for person in people_to_invite:
    print(f">>Dear {person.title()}, I would like to invite you to a dinner gathering at my home on Saturday, \nthe 15th, at 7 PM. It would be wonderful to have you with us!"
)

print(f'So, the total number of people coming is {len(people_to_invite)}')