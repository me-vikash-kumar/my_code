numbers=[i for i in range(1,10)]

for number in numbers: 
    if number == 1:
        print(f"{number}st\n")
    elif number == 2:
        print(f"{number}nd\n")
    elif number == 3:
        print(f"{number}rd\n")
    else:
        print(f"{number}th\n")