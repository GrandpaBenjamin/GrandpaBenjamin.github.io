#Life game

from Getting_Work import *
import Subway
import Bank
import pickle
import sys

print('Your life started')
while True:
    do = input()
    if do.lower() == 'get a job' or do.lower() == 'job' or do.lower() == 'get job':
        print('You go to the job office')
        get_job(salaries)
        
    elif do.lower() == 'work' or do.lower() == 'go to work':
        joob.work()
        
    elif do.lower() == 'go to subway' or do.lower() == 'subway':
        Subway.welcome()

    elif do.lower() == 'quit job' or do.lower() == 'leave job':
        joob.quit()

    elif do.lower() == 'go to bank' or do.lower() == 'bank' or do.lower() == 'go to the bank':
        Bank.goto()

    elif do == 'debug_MOOney':
        amount = input('$')
        amount = int(amount)
        money += amount
        pickle.dump(money, open("money.p","wb"))
        print('DEBUG MONEY HAS BEEN ADDED')
    elif do.lower() == 'die':
        print('You killed yourself')
        sys.exit()

'''

Things to fix:

- money from jobs (doesnt seem to add up when checking bal) -

'''
