from pokemon import Pokemon
from random import randint
class Arena:
    def __init__(self) -> None:
        pass
    def decide_who_play_next(self,player1:Pokemon,player2:Pokemon):
        p1 = player1.get_next_act()
        p1_priority = p1.get_priority()
        p2 = player2.get_next_act()
        p2_priority = p2.get_priority()
        if p1_priority > p2_priority: return player1,player2
        elif p2_priority < p1_priority: return player2,player1
        else:
            p1_placement = randint(0,1)
            if p1_placement == 0:
                return player1,player2
            else:
                return player2,player1