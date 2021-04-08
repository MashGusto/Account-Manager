import csv
import random

accounts = {}
with open('Accounts.csv', 'r') as f:
    for line in csv.reader(f):
        accounts[line[0]] = line[1]


def create(name, password):
    C_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters = list('abcdefghijklmnopqrstuvwxyz')
    nums = list('1234567890')
    s_chars = list('!@#$%^&*')

    valid = False
    while not valid:
        if password == '<generate>':
            passwordLst = []
            for i in range(10):
                passwordLst.append(random.choice([random.choice(C_letters), random.choice(letters), random.choice(nums),
                                                  random.choice(s_chars)]))
                password = ''.join(passwordLst)
        lp = password.lower()
        if len(lp) >= 8 and any((c in letters) for c in lp) and any((c in nums) for c in lp) and \
                any((c in s_chars) for c in lp):
            accounts[name] = password
            lst = []
            i = 1
            for key in accounts.keys():
                dictStr = ''
                if i < len(accounts):
                    dictStr = key + ',' + accounts[key] + '\n'
                else:
                    dictStr = key + ',' + accounts[key]
                    i += 1
                lst.append(dictStr)
            with open('Accounts.csv', 'w') as f:
                for string in lst:
                    f.write(string)
            print('New Account Created!\nName: ' + name + '\nPassword: ' + password)
            valid = True
        else:
            print(password)
            print('Password should contain at least 8 characters including letters, 1(minimum) special character'
                  '(!,@,#,$,%,^,& or *) and 1(minimum) number(0-9).')
            valid = True


def login(name, password):
    if name in accounts:
        if accounts.get(name) == password:
            print('Logged in successfully!')
        else:
            print('Wrong Password. Try again!')
    else:
        print('Account not found. Try creating one.')


print('Hello! Welcome to Mash Inc.')
print('Please login with your account(Input 1). If you are new, please register a new account(Input 2)')
option = int(input())
name = ''
password = ''
if option == 1:
    name = input('Please type your username: ')
    password = input('Please type your password: ')
    login(name, password)
elif option == 2:
    name = input('Please type your name: ')
    password = input('Please type your new password: ')
    create(name, password)
while option != 1 and option != 2:
    print('Invalid input.')
