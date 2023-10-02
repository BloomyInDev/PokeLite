from random import randint
from typing import Literal

class Pokemon_basics:
    types = ['normal','fire','water','grass','electric','rock']
    types_type_def = Literal['normal','fire','water','grass','electric','rock']
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
        self.__type:str = poke_type
        self.__life = life
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
    
class Pokemon:
    def __init__(self,pokemon_base:Pokemon_base,custom_name:str|None=None) -> None:
        self.__name = custom_name
        pass
    def get_name(self):
        return self.__name
    
class Pokemon_Attack:
    def __init__(self,name:str,damage:tuple[int,int],uses:tuple[int,int],shock_itself:tuple[bool,tuple[int,int]|None]) -> None:
        assert(isinstance(name,str))
        assert(isinstance(damage,tuple) & len(damage)==2)
        assert(isinstance(uses,tuple) & len(uses)==2)
        assert(isinstance(shock_itself,tuple))
        self.__shock_itself: dict[str, bool|tuple[int,int]] = {"enabled":shock_itself[0]}
        if shock_itself[0]==True:
            assert(isinstance(shock_itself[1],tuple))
            assert(len(shock_itself[1])==2)
            self.__shock_itself["damage"] = shock_itself[1]
        self.__name = name
        self.__damage = damage
        self.__max_uses = randint(uses[0],uses[1])
        self.__uses = self.__max_uses
        
        pass
    def attack(self,pokemon_attacked:Pokemon,):
        self.__uses -= 1
        return