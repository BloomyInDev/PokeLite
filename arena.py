from custom_attacks import Custom_Attack
from pokemon import Attack, Attack_Scheme, Pokemon, Pokemon_base
from effects import Effects
from random import randint
class Arena_Data:
    attack_list = {
        "charge":Attack_Scheme('Charge','normal', (30,35),(20,20),50,(False,None)),
        "trempette":Attack_Scheme('Trempette','water',(0,0),(40,40),50,(False,None)),
        "flameche":Custom_Attack.Attack_With_Effect('Flammèche','fire',(20,25),(25,25),50,(False,None),Effects.Burn()),
        "pistolet_a_o":Attack_Scheme('Pistolet à O','water',(20,25),(25,25),50,(False,None)),
        "etincelle":Attack_Scheme('Etincelle','electric',(20,25),(25,25),50,(False,None)),
        "belier":Attack_Scheme('Bélier','normal',(80,85),(15,15),50,(True,(15,20),)),
        "croc_fatal":Custom_Attack.Half_Life_Damage_Attack('Croc Fatal','normal',(10,10),50,(False,None)),
        "lance_flamme":Attack_Scheme('Lance Flamme','fire',(85,90),(15,15),50,(False,None)),
        "vive_attaque":Attack_Scheme('Vive-Attaque','normal',(35,40),(20,30),100,(False,None)),

    }
    pokemon_list = {
        "salameche":Pokemon_base("salameche",'Salamèche','fire',(114,146),[Attack(attack_list['charge']),Attack(attack_list['vive_attaque']),Attack(attack_list['flameche']),Attack(attack_list['lance_flamme'])]),
        "bulbizare":Pokemon_base("bulbizare",'Bulbizare','grass',(120,152),[Attack(attack_list['charge']),Attack(attack_list['vive_attaque'])]),
        "carapuce":Pokemon_base("carapuce",'Carapuce','water',(119,151),[Attack(attack_list['charge']),Attack(attack_list['vive_attaque'])]),
        "pikachu":Pokemon_base("pikachu",'Pikachu','electric',(95,145),[Attack(attack_list['charge']),Attack(attack_list['vive_attaque'])]),
        "magicarpe":Pokemon_base("magicarpe",'Magicarpe','water',(95,127),[Attack(attack_list['charge']),Attack(attack_list['vive_attaque'])]),
        "chrysapile":Pokemon_base("chrysapile",'Chrysapile','grass',(132,164),[Attack(attack_list['charge']),Attack(attack_list['vive_attaque'])]),
        "rattatac":Pokemon_base("rattatac",'Rattatac','normal',(130,162),[Attack(attack_list['charge']),Attack(attack_list['vive_attaque']),Attack(attack_list['croc_fatal'])]),
        "ectoplasma":Pokemon_base("ectoplasma",'Ectoplasma','ghost',(135,167),[Attack(attack_list['charge']),Attack(attack_list['vive_attaque'])])
    }
class Arena:
    def __init__(self) -> None:
        pass
    def choose_random_poke(self) -> Pokemon:
        list_poke = list(Arena_Data.pokemon_list.keys())
        id_list_poke = randint(0,len(list_poke)-1)
        return Pokemon(Arena_Data.pokemon_list[list_poke[id_list_poke]])
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