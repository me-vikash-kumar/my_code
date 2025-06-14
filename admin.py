from user_class import user
from Privileges import Privileges

class Administrator(user,Privileges):
    '''special case of user with extra privileges'''
    def __init__(self, first_name, last_name, gender, age, dob):
        super().__init__(first_name, last_name, gender, age, dob)
        Privileges.__init__(self)
        

if __name__ =="__main__":
    Kamaraja=Administrator('Kamaraja','Nadar','male','50','15-07-1915')
    Kamaraja.show_privileges()
    Kamaraja.describe_user()