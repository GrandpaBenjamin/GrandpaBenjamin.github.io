#subway chicken tendies

from time import sleep
from random import randint
import pickle
breads = ['9-Grain Wheat','Italian','Hearty Italian','Flatbread']
salads = ['Lettuce','Tomato','Cucumber','Olives','Pepper','Juicy']
meats = ['Pepperoni','Salami','Ham','Roast Beef','Turkey Breast','Carved Turkey','Tuna','Teriyaki Chicken','Rotisserie Chicken','Chicken Strips','Roasted Chicken','Meatballs','Steak','Peperoni','Corned Beef']
drinks = ['Fanta','Coke','Drench','Fruit Shoot','Mountain Dew','Water']
cookies = ['Double Chocolate Cookie','Chocolate Chip Cookie','Rainbow Gem Cookie','Raspberry Cheesecake Cookie','Oatmeal Raisin Cookie']
crisps = ['Cheese and Onion','Plain','Ready Salted','Salt and Vinegar']
premade_sandwiches = []
meal_price = 2
moneyy = pickle.load(open('money.p','rb'))


def in_Stock(to_check,compare_with):
    for x in compare_with:
        if x.lower() == to_check.lower():
            return True
        elif to_check.lower() == 'none':
            return True
    return False
def isint(x):
    try:
        int(x)
        return True
    except:
        return False
def chicken_tendies():
    while True:
        count = input('how many tendies do you want? ')
        if isint(count):
            counte = int(count)
            if counte > 1:
                print('so that\'ll be ' + count, 'tendies')
                break
            elif counte == 1:
                print('so that\'ll be ' + count, 'tendie')
                break
        else:
            continue
    payment_tendies(counte)
def welcome():
    cookie_or_crisp = ''
    moneyy = pickle.load(open('money.p','rb'))
    print('You card balance is',moneyy)
    print('hello welcome to subway')
    while True:
        size = input('Footlong or 6-inch? ')
        if size.lower() == 'footlong' or size.lower() == '6-inch':
            break
        elif size.lower() == 'chicken tendies':
            chicken_tendies()
            return
        else:
            print('wrong')
            continue
    while True:
        bread = input('What bread would you like? ')
        if in_Stock(bread,breads):
            break
        elif not(in_Stock(bread,breads)):
            print('That bread is not in stock')
            continue
        
    print('ok')
    while True:
        meat = input('What meat would you like? ')
        if in_Stock(meat,meats):
            break
        elif not(in_Stock(meat,meats)):
            print('We dont have that in stock')
            continue
    print('ok')
    while True:
        salad = input('What salad would you like? ')
        if in_Stock(salad,salads):
            break
        elif not(in_Stock(salad,salads)):
            print('That salad is not in stock')
            continue
    print('ok')
    while True:
        meal = input('Would you like to make that a meal? ')
        if meal.lower() == 'yes' or meal.lower() == 'yep':
            meal = True
            break
        elif meal.lower() == 'no' or meal.lower() == 'nope':
            meal == False
            break
        else:
            continue
    if meal:
        print('so you will make it a meal')
        while True:
            while True:
                drink = input('What drink would you like? ')
                if in_Stock(drink,drinks):
                    break
                elif not(in_Stock(drink,drinks)):
                    print('That drink is not in stock')
                    continue
            while True:
                side = input('Would you like a cookie or a packet of crisps? ')
                if side.lower() == 'cookie':
                    side = 'COOKIE'
                    break
                elif side.lower() == 'crisps' or side.lower() == 'packet of crisps':
                    side = 'CRISPS'
                    break
                else:
                    print('Sorry we only sell Cookies or Crisps as part of the meal deal')
                    continue
            if side == 'COOKIE':
                while True:
                    cookie = input('What cookie would you like? ')
                    if in_Stock(cookie,cookies):
                        cookie_or_crisp = cookie
                        break
                    elif not(in_Stock(cookie,cookies)):
                        print('That cookie is not in stock')
                        continue
                break
                    
            elif side == 'CRISPS':
                while True:
                    crisp = input('What crisps do you want? ')
                    if in_Stock(crisp,crisps):
                        cookie_or_crisp = crisp
                        break
                    elif not(in_Stock(crisp,crisps)):
                        print('That packet of crisps is not in stock')
                        continue
            else:
                break
    elif not(meal):
        print('ok')
        

    payment(bread,meat,salad,cookie_or_crisp,drink,size,meal)

def payment(bread,meat,salad,cookie_or_crisp,drink,size,meal, meal_price = meal_price,moneyy = moneyy):
    sandwich = [bread,meat,salad]
    cost = 0
    if bread != 'none':
        cost += 2

    if meat != 'none':
        cost += 3
        
    if salad != 'none':
        cost += 3

    if size.lower() == 'footlong':
        cost = cost * 2
        
    if meal == True:
        cost += 2
    print('')
    print('So you want a',size,'sandwich with',meat,'and',salad,'on',bread,'bread')
    if meal:
        print('With a ',drink,'and a',cookie_or_crisp)
    print('')
    print('That will be £'+ str(cost))
    money = moneyy - cost
    pickle.dump(money,open('money.p','wb'))
    print('Your new balance is',money)

def payment_tendies(count,moneyy = moneyy):
    single_tendie = 0.50
    cost = single_tendie * count
    print('')
    print('That will be £'+ str(cost))
    money = moneyy - cost
    pickle.dump(money,open('money.p','wb'))
    print('Your new balance is',money)
    
