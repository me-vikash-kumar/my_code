user_list=['H_R','admin','emplyee_1','emplyee_2','emplyee_3']
user_list_placeholder=user_list[:]
for user in user_list:
  
   name=user_list_placeholder.pop()
   if user == 'admin' :
 
       print(f'Hello {name} ,would you like to see status report.\n')

   else:
       print(f'Hello {name} ,thank you for joining.\n') 
       
