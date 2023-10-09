from os import get_terminal_size
from random import randint
from custom_attacks import Custom_Attack
from pokemon import Attack, Attack_Scheme, Pokemon_base, Pokemon
from arena import Arena

attack_list = {
    "charge":Attack_Scheme('Charge','normal', (30,35),(20,20),50,(False,None)),
    "trempette":Attack_Scheme('Trempette','water',(0,0),(40,40),50,(False,None)),
    "flameche":Attack_Scheme('Flammèche','fire',(20,25),(25,25),50,(False,None)),
    "pistolet_a_o":Attack_Scheme('Pistolet à O','water',(20,25),(25,25),50,(False,None)),
    "etincelle":Attack_Scheme('Etincelle','electric',(20,25),(25,25),50,(False,None)),
    "belier":Attack_Scheme('Bélier','normal',(80,85),(15,15),50,(True,(15,20),)),
    "croc_fatal":Custom_Attack.Half_Life_Damage_Attack('Croc Fatal','normal',(10,10),50,(False,None)),
    "lance_flamme":Attack_Scheme('Lance Flamme','fire',(85,90),(15,15),50,(False,None)),
    "vive_attaque":Attack_Scheme('Vive-Attaque','normal',(35,40),(20,30),100,(False,None)),

}
pokemon_list = {
    "salameche":Pokemon_base('Salamèche','fire',(114,146),[Attack(attack_list['charge']),Attack(attack_list['vive_attaque']),Attack(attack_list['flameche']),Attack(attack_list['lance_flamme'])]),
    #"bulbizare":Pokemon_base('Bulbizare','grass',(120,152)),
    #"carapuce":Pokemon_base('Carapuce','water',(119,151)),
    #"pikachu":Pokemon_base('Pikachu','electric',(95,145)),
    #"magicarpe":Pokemon_base('Magicarpe','water',(95,127)),
    #"chrysapile":Pokemon_base('Chrysapile','grass',(132,164)),
    "rattatac":Pokemon_base('Rattatac','normal',(130,162),[Attack(attack_list['croc_fatal']),Attack(attack_list['vive_attaque'])]),
    #"ectoplasma":Pokemon_base('Ectoplasma','ghost',(135,167))
}

class Main:
    def __init__(self) -> None:
        print("Pokemon - Lite Edition")
        self.spaces = '-'*20
        self.p1, self.p2 = self.choose_random_poke(), self.choose_random_poke()
        self.turn = 0
        print(f"Joueur 1 a {self.p1.get_name()}")
        print(f"Joueur 2 a {self.p2.get_name()}")
        self.game_loop()
        pass
    def choose_random_poke(self) -> Pokemon:
        list_poke = list(pokemon_list.keys())
        id_list_poke = randint(0,len(list_poke)-1)
        return Pokemon(pokemon_list[list_poke[id_list_poke]])
    def game_loop(self):
        if self.p1.get_life() == 0:
            print('Partie terminée, Joueur 2 a gagné !')
            return
        if self.p2.get_life() == 0:
            print('Partie terminée, Joueur 1 a gagné !')
            return
        p1_text = f'J1:{self.p1.get_name()},HP:{self.p1.get_life()}/{self.p1.get_max_life()}'
        p2_text = f'J2:{self.p2.get_name()},HP:{self.p2.get_life()}/{self.p2.get_max_life()}'
        spacing:str = ' '*(get_terminal_size()[0]-(len(p1_text)+len(p2_text))-4)
        player_playing = (self.turn%2)+1
        player_playing_obj = self.p1 if player_playing==1 else self.p2
        
        if self.turn%2==0 and self.turn != 0:
            playing_order = Arena().decide_who_play_next(self.p1,self.p2)
            playing_order[0].use_next_act(playing_order[1])
            playing_order[1].use_next_act(playing_order[0])
            
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
                self.game_loop()
            case 3:
                pass
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