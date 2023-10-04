from os import get_terminal_size
from random import randint
from pokemon import Pokemon_base, Pokemon_Attack, Pokemon

attack_list = {
    "charge":Pokemon_Attack('Charge','normal', (30,35),(20,20),50,(False,None)),
    "trempette":Pokemon_Attack('Trempette','water',(0,0),(40,40),50,(False,None)),
    "flameche":Pokemon_Attack('Flammèche','fire',(20,25),(25,25),50,(False,None)),
    "pistolet a o":Pokemon_Attack('Pistolet à O','water',(20,25),(25,25),50,(False,None)),
    "etincelle":Pokemon_Attack('Etincelle','electric',(20,25),(25,25),50,(False,None)),
    "belier":Pokemon_Attack('Bélier','normal',(80,85),(15,15),50,(True,(15,20),)),
    #"croc fatal":Pokemmon_Attack('Croc Fatal','normal',(),(10,10),50,(False,None)),
    "lance_flamme":Pokemon_Attack('Lance Flamme','fire',(85,90),(15,15),50,(False,None)),
    "vive_attaque":Pokemon_Attack('Vive-Attaque','normal',(35,40),(20,30),100,(False,None)),

}
pokemon_list = {
    "salameche":Pokemon_base('Salamèche','fire',(114,146)),
    "bulbizare":Pokemon_base('Bulbizare','grass',(120,152)),
    "carapuce":Pokemon_base('Carapuce','water',(119,151)),
    "pikachu":Pokemon_base('Pikachu','electric',(95,145)),
    "magicarpe":Pokemon_base('Magicarpe','water',(95,127)),
    "chrysapile":Pokemon_base('Chrysapile','grass',(132,164)),
    "rattatat":Pokemon_base('Rattatac','normal',(130,162)),
    "ectoplasma":Pokemon_base('Ectoplasma','ghost',(135,167))
}
def choose_random_poke() -> Pokemon:
    list_poke = list(pokemon_list.keys())
    id_list_poke = randint(0,len(list_poke)-1)
    return Pokemon(pokemon_list[list_poke[id_list_poke]])
#poke = Pokemon_base('coucou','air',(1500,2000))
print("Pokemon - Lite Edition")
spaces = '-'*20
p1, p2 = choose_random_poke(), choose_random_poke()
print(f"Joueur 1 a {p1.get_name()}")
print(f"Joueur 2 a {p2.get_name()}")
p1_text = f'J1:{p1.get_name()},HP:{p1.get_life()}/{p1.get_max_life()}'
p2_text = f'J2:{p2.get_name()},HP:{p2.get_life()}/{p2.get_max_life()}'
spacing:str = ' '*(get_terminal_size()[0]-(len(p1_text)+len(p2_text))-4)
top_text = f'  {p1_text}{spacing}{p2_text}  \n'
print(f'{top_text}',end='\r')
#print(f"{spaces}\nTour de Joueur 1\n{spaces}")
#print(f'Attaquer\nQue voulez vous faire ?')