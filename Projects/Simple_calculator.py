'''Simple Calculator'''

print(r'''
   _____ _                 __                     
  / ___/(_)___ ___  ____  / /__                   
  \__ \/ / __ `__ \/ __ \/ / _ \                  
 ___/ / / / / / / / /_/ / /  __/                  
/____/_/_/ /_/ /_/ .___/_/\___/                   
   ______      _/_/         __      __            
  / ____/___ _/ /______  __/ /___ _/ /_____  _____
 / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
/ /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
\____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     ''')

def addition(a,b):
    return f'Result of this addition is {a+b}'

def subtraction(a,b):
    return f'Result of this subtraction is {a-b}'

def multiplication(a,b):
    return f'Result of this multiplication is {a*b}'

def division(a,b):
    if b==0 :
        return  '\n***Cannot divide by zero***\n'
    return f'Result of this division is {a/b}'


while True:
    print("="*90)


    print("Choose the type of calculation you want to perform:")

    print  ('''
  Enter 1 for Addition
        2 for Subtraction
        3 for Multiplication
        4 for Division
        5 for Exit
              ''')
    try:
        calculation_type=int(input('Enter your choice: '))
    except ValueError:
        print('Invalid input. Please enter a number.')
        input('press enter to continue...')
        continue
            
    if calculation_type == 5:
        break
    elif calculation_type == 1:      
        print(f'first number + second number = ')              
        a=int(input('Enter first number: '))
        b=int(input('Enter second number: '))
        print(addition(a,b))
        input('press enter to continue...')
    elif calculation_type== 2:
        print(f'first number - second number = ')
        a=int(input('Enter first number: '))
        b=int(input('Enter second number: '))
        print(subtraction(a,b))
        input('press enter to continue...')
    elif calculation_type== 3:
        print(f'first number * second number = ')
        a=int(input('Enter first number: '))
        b=int(input('Enter second number: '))
        print(multiplication(a,b))
        input('press enter to continue...')
    elif calculation_type== 4:
        print(f'first number / second number = ')
        a=int(input('Enter first number: '))
        b=int(input('Enter second number: '))
        print(division(a,b))
        input('press enter to continue...')
    else:
        print('Please provide a valid input e.g 1,2,3,4,5]')
        input('press enter to continue...')

