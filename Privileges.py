class Privileges:
    def __init__(self):
        self.privileges=['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Admin has following privileges:')
        for i,j in enumerate(self.privileges):
            print(f'{i+1}. {j}')
        print('='*20)





    