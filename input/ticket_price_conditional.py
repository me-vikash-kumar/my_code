
i=7
while True:
   i=i-1

   age = int(input("Enter your age:"))    
   if age>1 and age <= 3 :
        print("Entry is free for children less than 3 years old")
   elif age >3 and age <=12:
        print("Entry fee is $10")
   elif age>12:
        print('Your Entry fee is $15')
   elif i==0:
        break
   else:
        age =00
        print("This is an invalid age!")
        break