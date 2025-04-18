people_to_invite =['leonardo da vinci','jorden b peterson','jeffrey kaplan','joshua meyer']

person_unable_to_come ='leonardo da vinci'

person_to_invite_instead="Some asian dude"

print(f'Hi {person_unable_to_come}, I completely understand that you can''t make it to dinner. While we''ll miss your company\n,I hope everything is well with you and that we can catch up sometime soon. Take care and looking forward to seeing you next time! ')

people_to_invite.remove(person_unable_to_come)

people_to_invite.append(person_to_invite_instead)

for person in people_to_invite:


    print(f">>Dear {person.title()}, I would like to invite you to a dinner gathering at my home on Saturday, \nthe 15th, at 7 PM. It would be wonderful to have you with us!"
)