current_user=['manoj75','rajesh60','suresh7','umashankar09','surendra75']
new_user=['kolar_63','hijra','rajesh60','suresh7','umashankar09','jane_09']
current_user_lower=[user.lower() for user in current_user]
for user in new_user:
    if user.lower() in current_user_lower:
        print(f'{user} is already taken.\n')
    else:
        print(f'{user} is available.\n')

print(current_user_lower)