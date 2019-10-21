import password
l=int(input('How long do you want your password to be?'))
print('Your password is:')

while True:
    pas=password.genPassword(l)
    print(pas)
    anw=input('Accept the password? (Y/N)')
    if anw=='Y':
        print('Please remember your password:')
        print(pas)
        break
    elif anw=='N':
        continue
    else:
        pass
