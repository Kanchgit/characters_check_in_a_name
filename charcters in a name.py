name = input('Enter the name :' )

print(len(name))
if len(name) < 3:
    print('Name should be more than 3 characters')
elif len(name)> 20:
    print('Name should be max of 50 characters')
else:
    print('Good Name')