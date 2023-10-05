from os import get_terminal_size
from random import randint
from pokemon import Pokemon_base, Pokemon_attack, Pokemon
from custom_attacks import Custom_Attack

attack_list = {
    "charge":Pokemon_attack('Charge','normal', (30,35),(20,20),50,(False,None)),
    "trempette":Pokemon_attack('Trempette','water',(0,0),(40,40),50,(False,None)),
    "flameche":Pokemon_attack('Flammèche','fire',(20,25),(25,25),50,(False,None)),
    "pistolet a o":Pokemon_attack('Pistolet à O','water',(20,25),(25,25),50,(False,None)),
    "etincelle":Pokemon_attack('Etincelle','electric',(20,25),(25,25),50,(False,None)),
    "belier":Pokemon_attack('Bélier','normal',(80,85),(15,15),50,(True,(15,20),)),
    "croc_fatal":Custom_Attack.Half_Life_Damage_Attack('Croc Fatal','normal',(10,10),50,(False,None)),
    "lance_flamme":Pokemon_attack('Lance Flamme','fire',(85,90),(15,15),50,(False,None)),
    "vive_attaque":Pokemon_attack('Vive-Attaque','normal',(35,40),(20,30),100,(False,None)),

}
pokemon_list = {
    "salameche":Pokemon_base('Salamèche','fire',(114,146),[attack_list['charge'],attack_list['vive_attaque'],attack_list['flameche'],attack_list['lance_flamme']]),
    "bulbizare":Pokemon_base('Bulbizare','grass',(120,152)),
    "carapuce":Pokemon_base('Carapuce','water',(119,151)),
    "pikachu":Pokemon_base('Pikachu','electric',(95,145)),
    "magicarpe":Pokemon_base('Magicarpe','water',(95,127)),
    "chrysapile":Pokemon_base('Chrysapile','grass',(132,164)),
    "rattatac":Pokemon_base('Rattatac','normal',(130,162)),
    "ectoplasma":Pokemon_base('Ectoplasma','ghost',(135,167))
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
        p1_text = f'J1:{self.p1.get_name()},HP:{self.p1.get_life()}/{self.p1.get_max_life()}'
        p2_text = f'J2:{self.p2.get_name()},HP:{self.p2.get_life()}/{self.p2.get_max_life()}'
        spacing:str = ' '*(get_terminal_size()[0]-(len(p1_text)+len(p2_text))-4)
        player_playing = (self.turn%2)+1
        top_text = f'  {p1_text}{spacing}{p2_text}  \n'
        middle_text = f'C\'est au tour du joueur {player_playing}'
        bottom_text = f'Quel action faire ?\n1.Attaquer / 2.Objets / 3.Pokemon / 4.Capitulation\n>>'
        print(f'{top_text}\n{middle_text}\n',end='\r')
        response = int(input(bottom_text))
        match response:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case _:
                self.game_loop()
        self.turn += 1
        self.game_loop()
        

#print(f"{spaces}\nTour de Joueur 1\n{spaces}")
#print(f'Attaquer\nQue voulez vous faire ?')
Main()