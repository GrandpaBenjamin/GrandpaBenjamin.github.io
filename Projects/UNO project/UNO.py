#UNO defintions

from random import randint


played_cards = []

cards = {1 : "RED 1",
         2 : "RED 2",
         3 : "RED 3",
         4 : "RED 4",
         5 : "RED 5",
         6 : "RED 6",
         7 : "RED 7",
         8 : "RED 8",
         9 : "RED 9",
         10 : "RED Rev",
         11 : "RED draw-2",
         12 : "RED draw-2",
         13 : "RED Rev",
         14 : "RED 1",
         15 : "RED 2",
         16 : "RED 3",
         17 : "RED 4",
         18 : "RED 5",
         19 : "RED 6",
         20 : "RED 7",
         21 : "RED 8",
         22 : "RED 9",
         23 : "RED Skip",
         24 : "RED 0",
         25 : "BLUE 1",
         26 : "BLUE 2",
         27 : "BLUE 3",
         28 : "BLUE 4",
         29 : "BLUE 5",
         30 : "BLUE 6",
         31 : "BLUE 7",
         32 : "BLUE 8",
         33 : "BLUE 9",
         34 : "BLUE Rev",
         35 : "BLUE draw-2",
         36 : "BLUE draw-2",
         37 : "BLUE Rev",
         38 : "BLUE 1",
         39 : "BLUE 2",
         40 : "BLUE 3",
         41 : "BLUE 4",
         42 : "BLUE 5",
         43 : "BLUE 6",
         44 : "BLUE 7",
         45 : "BLUE 8",
         46 : "BLUE 9",
         47 : "BLUE 0",
         48 : "BLUE Skip",
         49 : "GREEN 1",
         50 : "GREEN 2",
         51 : "GREEN 3",
         52 : "GREEN 4",
         53 : "GREEN 5",
         54 : "GREEN 6",
         55 : "GREEN 7",
         56 : "GREEN 8",
         57 : "GREEN 9",
         58 : "GREEN Rev",
         59 : "GREEN draw-2",
         60 : "GREEN draw-2",
         61 : "GREEN Rev",
         62 : "GREEN 1",
         63 : "GREEN 2",
         64 : "GREEN 3",
         65 : "GREEN 4",
         66 : "GREEN 5",
         67 : "GREEN 6",
         68 : "GREEN 7",
         69 : "GREEN 8",
         70 : "GREEN 9",
         71 : "GREEN 0",
         72 : "GREEN Skip",
         73 : "YELLOW 1",
         74 : "YELLOW 2",
         75 : "YELLOW 3",
         76 : "YELLOW 4",
         77 : "YELLOW 5",
         78 : "YELLOW 6",
         79 : "YELLOW 7",
         80 : "YELLOW 8",
         81 : "YELLOW 9",
         82 : "YELLOW Rev",
         83 : "YELLOW draw-2",
         84 : "YELLOW draw-2",
         85 : "YELLOW Rev",
         86 : "YELLOW 1",
         87 : "YELLOW 2",
         89 : "YELLOW 3",
         90 : "YELLOW 4",
         91 : "YELLOW 5",
         92 : "YELLOW 6",
         93 : "YELLOW 7",
         94 : "YELLOW 8",
         95 : "YELLOW 9",
         96 : "YELLOW 0",
         97 : "YELLOW Skip",
         98 : "YELLOW Skip",
         99 : "BLUE Skip",
         100 : "GREEN Skip",
         101 : "RED Skip",
         102 : "WILD",
         103 : "WILD",
         104 : "WILD",
         105 : "WILD",
         106 : "DRAW 4",
         107 : "DRAW 4",
         108 : "DRAW 4",
         109 : "DRAW 4"
}
class Player:
    def __init__(self,PlayerNom):
        self.PlayerNom = PlayerNom
        self.PlayerCards = []
        
    def starting_cards(self):
        for x in range(7):
            self.PlayerCards.append(cards.get(randint(1,109)))
        StartingCards = self.PlayerCards
        self.show_cards(StartingCards)
    def show_cards(self, StartingCards):
        print(StartingCards)
            
NomOCards = 109
def pick_card(NomOCards):
    pickup = randint(1,NomOCards)
    return pickup

def startUp():
    P1 = Player(1)
    P1.starting_cards()

startUp()
