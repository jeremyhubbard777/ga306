name = input('what is your name\n')
age = int(input('what is your age\n'))
new_age = age + 1
if age < 21:
    print('You are',age,'years old.','You are just a baby', name+'.','Naxt year you will be',new_age,'years old.')

elif age == 21:
    print('You are',age,'years old.','You can drink now', name+'.','Naxt year you will be',new_age,'years old.')

else:
    print('You are',age,'years old.','Wow! You are old', name+'.','Naxt year you will be',new_age,'years old.')