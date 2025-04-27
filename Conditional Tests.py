#First conditional test

world='Round'

if world.lower()=='round':
    print(f'\nworld is round statement is {bool(world.lower()=='round')}')

#2nd test
if world.lower()!='flat':
    print(f'\nworld is not flat statement is {bool(world.lower()!='flat')}')

age_david = 17

age_james = 21

#3rd test
print(f'\nOne of you, either James or David, is greater than or equal to 21 years of age.? \n{bool(age_david>=21 or age_james>=21)}')

#4th test
print(f'\nOne of you, either James or David, is greater than or equal to 18 years of age.? \n{bool(age_david>=18 or age_james>=18)}\n')

#5th test
if age_james >21 :
    print(f"James is 21 at least years:this statement is {bool(age_james >21)}")
else :
    print(f"James is 21 at least years:this statement is {bool(age_james >21)}")

#6th conditional test 

current_in_line1 = 10

current_in_line2 = 5

print(f"\nThe machine will only carry load if current is adequate in both line")

if current_in_line1 >=10 and current_in_line2 >=10 :
    print(f"The machine will operate : {bool(current_in_line1 >=10 and current_in_line2 >=10)}")

else:
    print(f"\nThe machine will operate : {bool(current_in_line1 >=10 and current_in_line2 >=10)}")

#7th condition
print(f'is 5< 2 :{bool(5<2)}')

#8th condition
print(f'is 5>2:{bool(5>2)}')

#9th condition
print(f'is 15.0>=(30/2):{bool(15>=(30/2))}')

#10th condition 
print(f'Is 11 an odd number?:{bool (11%2)} ')

bike = "honda"

print(f'is that bike a honda ? :{bool(bike=="honda")}')

print(f'is this bike a honda ? :{bool(bike=="TVS")}')

cycle = "Hercules"

print(f'is that cycle a hercules cycle ? :{bool(cycle.lower()=="hercules")}')

print(f'is that cycle a hercules cycle ? :{bool(cycle.lower=="Avon")}')

print(f"number 6>=3 :{bool(6>=3)}")

print(f"number 5==4 :{bool(5==4)}")

print(f"number 9>4 :{bool(9>4)}")

print(f"number 14!=50 :{bool(14!=50)}")

print(f"number 36<21 :{bool(36<21)}")

print(f"number 9<9 :{bool(9<9)}")

print(f"number 9<=9 :{bool(9<=9)}")

items = ["Laptop", "Umbrella", "Notebook", "Coffee Mug", "Tennis Ball", "Headphones", 
         "Guitar", "Skateboard", "Backpack", "Camera"]

print(f"is headphone in items :{bool("headphones" in [item.lower() for item in items])}")

print(f"is pen in items :{bool("pen" in [item.lower() for item in items])}")

print(f"is camera is not in items :{bool("camera" not in [item.lower() for item in items])}")

print(f"is banana is not in items :{bool("banana" not in [item.lower() for item in items])}")