favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

should_take_poll = ['jen','phil','bob','alice','carol']

for name in should_take_poll:

    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for taking the poll.\n")
    else:
        print(f"{name.title()}, please take our poll.\n")