#Getting_Work

#Modules
from random import randint as r
import pickle

#Variables
global moneyy
moneyy = pickle.load(open("money.p","rb"))
global employed
employed = False
global qualification
qualification = 'none'

#Dictionaries
jobs = {1: 'Bin Man',
        2: 'Lawyer',
        3: 'Doctor',
        4: 'Accountant',
        5: 'Nurse',
        6: 'Chemist',
        7: 'Artist',
        8: 'Animator',
        9: 'Cabin Crew',
        10: 'Scientist',
        11: 'Engineer',
        12: 'Teacher',
        13: 'Banker',
        14: 'Counsellor',
        15: 'Customs Officer',
        16: 'Dentist',
        17: 'Estate Agent',
        18: 'Forensic Scientist',
        19: 'Baker',
        20: 'Illustrator',
        21: 'Programmer',
        22: 'IT support',
        23: 'Pharmacist',
        24: 'Photographer',
        25: 'Police Officer',
}

salaries = {'Bin Man': 4,
        'Lawyer': 100,
        'Doctor': 80,
        'Accountant': 60,
        'Nurse': 50,
        'Chemist': 65,
        'Artist': 15,
        'Animator': 20,
        'Cabin Crew': 34,
        'Scientist': 50,
        'Engineer': 45,
        'Teacher': 10,
        'Banker': 56,
        'Counsellor': 30,
        'Customs Officer': 35,
        'Dentist': 65,
        'Estate Agent': 36,
        'Forensic Scientist': 87,
        'Baker': 19,
        'Illustrator': 1,
        'Programmer': 200,
        'IT support': 23,
        'Pharmacist': 40,
        'Photographer': 24,
        'Police Officer': 40,
        'null': 0,
}
#Lists
available_jobs = [jobs.get(r(1,25)),jobs.get(r(1,25)),jobs.get(r(1,25)),jobs.get(r(1,25)),jobs.get(r(1,25))]

#Classes
class job:
    def __init__(self,name,desc,hourly_rate,employed = employed):
        self.name = name
        self.desc = desc
        self.hourly_rate = hourly_rate
        self.employed = employed
        self.employed = False

    def work(self,money = moneyy):
        if self.employed:
            time = r(1,9)
            moneyyyy = time*self.hourly_rate
            if time != 1:
                print(f'You worked for {time} hours')
            elif time == 1:
                print(f'You worked for {time} hour')
            print(f'You earnt ${moneyyyy}')
            moni = money + moneyyyy
            pickle.dump(moni,open("money.p","wb"))
        elif not(self.employed):
            print('You dont work here')
    def quit(self):
        if self.employed == True:
            how = input('How would you like to quit? ')
            if how.lower() == 'angrily':
                print('You stormed into your boss\' office')
                print('You quitted - he didnt care')
            elif how.lower() == 'calmly':
                print('You walked calmly into you boss\' office')
                print('You told him you wanted to quit - he was sad and wanted you to stay')
                print('You quitted')
            else:
                print('You walked into your boss\' office')
                print('You quitted')
            self.employed = False
        else:
            print('You dont have a job to quit')
def get_job(salary):
    available_jobs = [jobs.get(r(1,25)),jobs.get(r(1,25)),jobs.get(r(1,25)),jobs.get(r(1,25)),jobs.get(r(1,25))]
    print('Hello. Here is the list of available jobs:')
    one_job = available_jobs[0]
    second_job = available_jobs[1]
    third_job = available_jobs[2]
    fourth_job = available_jobs[3]
    fifth_job = available_jobs[4]
    print('1)',one_job)
    print('2)',second_job)
    print('3)',third_job)
    print('4)',fourth_job)
    print('5)',fifth_job)
    job_choice = input('Which job wll you be taking? ')
    if job_choice == '1':
        chance = r(1,10)
        if chance <= 6:
            joob.name = one_job
            joob.hourly_rate = salary.get(one_job)
            joob.employed = True
            print('You got the job yay')
        else:
            print('sorry you did not get the job')
        print('you walked out of the center')
    elif job_choice == '2':
        chance = r(1,10)
        if chance <= 6:
            joob.name = second_job
            joob.hourly_rate = salary.get(second_job)
            joob.employed = True
            print('You got the job yay')
        else:
            print('sorry you did not get the job')
        print('you walked out of the center')
    elif job_choice == '3':
        chance = r(1,10)
        if chance <= 6:
            joob.name = third_job
            joob.hourly_rate = salary.get(third_job)
            joob.employed = True
            print('You got the job yay')
        else:
            print('sorry you did not get the job')
        print('you walked out of the center')
    elif job_choice == '4':
        chance = r(1,10)
        if chance <= 6:
            joob.name = fourth_job
            joob.hourly_rate = salary.get(fourth_job)
            joob.employed = True
            print('You got the job yay')
        else:
            print('sorry you did not get the job')
        print('you walked out of the center')
    elif job_choice == '5':
        chance = r(1,10)
        if chance <= 6:
            joob.name = fifth_job
            joob.hourly_rate = salary.get(fifth_job)
            joob.employed = True
            print('You got the job yay')
        else:
            print('sorry you did not get the job')
        print('you walked out of the center')
    elif job_choice == 'nevermind' or job_choice == 'none' or job_choice == 'no':
        print('You walked away from the job offers')
        print('You left the room')
    else:
        print('if your not going to take this offer seriously then leave.')
        print('you walked slowly and sadly out of the room - this is so sad')






joob = job('null','why did i put this here',salaries.get('null'))
