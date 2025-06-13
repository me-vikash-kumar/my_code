class user :
    def __init__(self,first_name,last_name,gender,age,dob):
        self.first_name=first_name
        self.last_name=last_name        
        self.gender=gender
        self.age=age
        self.dob=dob
        self.login_attempts=0
    
    def describe_user(self):
        print("Name : "+self.first_name+" "+self.last_name)
        print("Gender : "+self.gender)
        print("Age : "+str(self.age))
        print("Date of Birth : "+self.dob)

    def greet_user(self):
        print("Hello "+self.first_name+" "+self.last_name+"!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def login_reset(self):
        self.login_attempts=0
        
ramesh=user('ramesh','tiwari','male','25','12-03-1995')

ramesh.describe_user()

ramesh.increment_login_attempts()
ramesh.increment_login_attempts()
ramesh.increment_login_attempts()
ramesh.increment_login_attempts()
ramesh.increment_login_attempts()
print(ramesh.login_attempts)

ramesh.login_reset()

print(ramesh.login_attempts)