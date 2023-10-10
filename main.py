from os import get_terminal_size
from arena import Arena

class Main:
    def __init__(self) -> None:
        print("Pokemon - Lite Edition")
        self.p1, self.p2 = Arena().choose_random_poke(), Arena().choose_random_poke()
        self.turn = 0
        print(f"Joueur 1 a {self.p1.get_name()}")
        print(f"Joueur 2 a {self.p2.get_name()}")
        self.game_loop()
        pass
    def game_loop(self):
        if self.p1.get_life() == 0:
            print('Partie terminée, Joueur 2 a gagné !')
            return
        if self.p2.get_life() == 0:
            print('Partie terminée, Joueur 1 a gagné !')
            return
        player_playing = (self.turn%2)+1
        player_playing_obj = self.p1 if player_playing==1 else self.p2
        
        if self.turn%2==0 and self.turn != 0:
            playing_order = Arena().decide_who_play_next(self.p1,self.p2)
            playing_order[0].execute_next_turn(playing_order[1])
            playing_order[1].execute_next_turn(playing_order[0])
        
        p1_text = f'J1:{self.p1.get_name()},HP:{self.p1.get_life()}/{self.p1.get_max_life()}'
        p2_text = f'J2:{self.p2.get_name()},HP:{self.p2.get_life()}/{self.p2.get_max_life()}' 
        spacing:str = ' '*(get_terminal_size()[0]-(len(p1_text)+len(p2_text))-4)   
        top_text = f'  {p1_text}{spacing}{p2_text}  \n'
        middle_text = f'C\'est au tour du joueur {player_playing}'
        bottom_text = ''
        question_text = f'Quel action faire ?\n1.Attaquer / 2.Objets / 3.Pokemon / 4.Capitulation\n>>'
        print(f'{top_text}\n{middle_text}\n{bottom_text}')
        response = int(input(question_text))
        match response:
            case 1:
                question2_text: str = f'Quelle attaque faire ?\n'
                bottom_text = 'Vous décidez d\'attaquer'
                list_atk: str = ''
                for i,e in enumerate(player_playing_obj.get_attacks()):
                    list_atk += f'{i+1}. {e.get_name()}, {e.get_type()}, Util.:{e.get_uses()}/{e.get_max_uses()}'
                    if i != len(player_playing_obj.get_attacks())-1:
                        list_atk+=' // '
                print(f'{top_text}\n{middle_text}\n{bottom_text}\n',end='\r')
                response = int(input(f'{question2_text}{list_atk}\n>>'))
                player_playing_obj.set_next_act(player_playing_obj.get_attacks()[response-1])
            case 2:
                print('Cette fonctionalité n\'existe pas')
                self.game_loop()
            case 3:
                print('Cette fonctionalité n\'existe pas')
                self.game_loop()
            case 4:
                print(f'Vous abandonez, {player_playing} a perdu !')
                return
            case _:
                self.game_loop()
        self.turn += 1
        self.game_loop()
        

#print(f"{spaces}\nTour de Joueur 1\n{spaces}")
#print(f'Attaquer\nQue voulez vous faire ?')
Main()