from random import randint
from typing import Literal

class Pokemon_basics:
    types = ['normal','fire','water','grass','electric','rock','ghost']
    types_type_def = Literal['normal','fire','water','grass','electric','rock','ghost']
    type_bonus_malus: dict[str, dict[str, types_type_def|None] | dict[str, str]] = {
        'normal':{'bonus':None,'malus':None},
        'fire':{'bonus':'grass','malus':'water'},
        'water':{'bonus':''}
    }

class Pokemon_base:
    def __init__(self,name:str,poke_type:Pokemon_basics.types_type_def,life:tuple[int,int]) -> None:
        assert(isinstance(name,str))
        assert(isinstance(poke_type,str))
        assert(isinstance(life,tuple) and len(life) == 2)
        assert(poke_type in Pokemon_basics.types)
        self.__name = name
        self.__type: str = poke_type
        self.__life: tuple[int, int] = life
        pass
    
    def get_name(self):
        return self.__name
    def set_name(self,name:str):
        assert(isinstance(name,str))
        self.__name = name
    
    def get_type(self):
        return self.__type
    def set_type(self,poke_type:str):
        assert(isinstance(poke_type,str))
        assert(poke_type in Pokemon_basics.types)
        self.__type = poke_type
    
    def get_life(self) -> tuple[int, int]:
        return self.__life

    
    
class Pokemon:
    def __init__(self,pokemon_base:Pokemon_base,custom_name:str|None=None) -> None:
        self.__poke = pokemon_base
        self.__name = custom_name or pokemon_base.get_name()
        self.__max_life = randint(self.__poke.get_life()[0],self.__poke.get_life()[1])
        self.__life = self.__max_life
        pass
    def get_max_life(self):
        return self.__max_life
    def get_life(self):
        return self.__life
    def set_life(self,life:int):
        assert(isinstance(life,int))
        self.__life = life
        
    def get_name(self):
        return self.__name
    
class Pokemon_Attack:
    def __init__(self,name:str,typeatk:Pokemon_basics.types_type_def,damage:tuple[int,int],uses:tuple[int,int],priority:int,shock_itself:tuple[bool,tuple[int,int]|None]) -> None:
        assert(isinstance(name,str))
        assert(typeatk in Pokemon_basics.types)
        assert(isinstance(damage,tuple) and len(damage) == 2)
        assert(isinstance(uses,tuple) and len(uses)==2)
        assert(isinstance(priority,int) and priority in range(0,100))
        assert(isinstance(shock_itself,tuple))
        self.__shock_itself: dict[str, bool|tuple[int,int]] = {"enabled":shock_itself[0]}
        if shock_itself[0]==True:
            assert(isinstance(shock_itself[1],tuple))
            assert(len(shock_itself[1])==2)
            self.__shock_itself["damage"] = shock_itself[1]
        self.__name = name
        self.__typeatk = typeatk
        self.__damage = damage
        self.__max_uses = randint(uses[0],uses[1])
        self.__uses = self.__max_uses
        
        pass
    def attack(self,pokemon_attacked:Pokemon,):
        self.__uses -= 1
        return