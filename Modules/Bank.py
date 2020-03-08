#Bank Module

import pickle
from random import randint


def goto():
    account = pickle.load(open('account.p','rb'))
    money = pickle.load(open('money.p','rb'))
    print('You go to the bank')
    doop = input('What do you want to do? ')
    if doop.lower() == 'save' or doop.lower() == 'deposit money':
        tries = 0
        if account == True:
            pin = pickle.load(open('pin.p','rb'))
            while tries < 4:
                enter_pin = input('Enter your pin: ')
                if enter_pin == pin:
                    print('Pin correct')
                    pin_correct()
                    break
                else:
                    tries += 1
                    tries_left = 3 - tries
                    print('You have',tries_left,'tries left')
        else:
            print('You do not have an account')
            print('You leave the bank')
            
        
    elif doop.lower() == 'get an account' or doop.lower() == 'get a bank account':
        if account == False:
            print('You walked to the bank man')
            print('He gave you a bank account')
            dig1 = str(randint(1,9))
            dig2 = str(randint(1,9))
            dig3 = str(randint(1,9))
            dig4 = str(randint(1,9))
            pin = dig1+dig2+dig3+dig4
            pickle.dump(pin, open('pin.p','wb'))
            print('Your pin is',pin)
            account = True
            pickle.dump(account,open("account.p","wb"))
            print('You left the bank')
        elif account == True:
            print('You already have an account')

    elif doop.lower() == 'what is my pin' or doop.lower() == 'i have forgotten my pin' or doop.lower() == 'pin':
        pin = pickle.load(open('pin.p','rb'))
        print('yout pin is',pin)

    else:
        print('You got confused and left the bank')
def pin_correct():
    print('1) Deposit Money')
    print('2) Check Balance')
    print('3) Quit')
    while True:
        dooop = input()
        if dooop == '1':
            print('Money has been deposited')
            
        elif dooop == '2':
            money = pickle.load(open('money.p','rb'))
            print('You balance is',money)
            
        elif dooop == '3':
            print('You closed the machine and left the bank')
            break
