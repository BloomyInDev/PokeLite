from __future__ import annotations
from random import randint, sample
from typing import Callable, Literal
from effects import Effects


class Pokemon_basics:
    types = ['normal','fire','water','grass','electric','rock','ghost']
    types_type_def = Literal['normal','fire','water','grass','electric','rock','ghost']
    type_bonus_malus: dict[str, dict[str, types_type_def|None] | dict[str, str]] = {
        'normal':{'bonus':None,'malus':None},
        'fire':{'bonus':'grass','malus':'water'},
        'water':{'bonus':''}
    }

class Pokemon_base:
    def __init__(self,name:str,poke_type:Pokemon_basics.types_type_def,life:tuple[int,int],atk_list:list[Attack]=[]) -> None:
        assert(isinstance(name,str))
        assert(isinstance(poke_type,str))
        assert(isinstance(life,tuple) and len(life) == 2)
        assert(poke_type in Pokemon_basics.types)
        assert(isinstance(atk_list,list))
        for e in atk_list:
            assert(isinstance(e,Attack) or True),f'{e}'
        self.__name = name
        self.__type: str = poke_type
        self.__atk_list = atk_list
        self.__life: tuple[int, int] = life
        pass
    
    def get_name(self):
        return self.__name
    
    def get_type(self):
        return self.__type
    def set_type(self,poke_type:str):
        assert(isinstance(poke_type,str))
        assert(poke_type in Pokemon_basics.types)
        self.__type = poke_type
    
    def get_life(self) -> tuple[int, int]:
        return self.__life
    def get_atk_list(self):
        return self.__atk_list
    
class Pokemon:
    def __init__(self,pokemon_base:Pokemon_base,custom_name:str|None=None) -> None:
        self.__poke = pokemon_base
        self.__name = custom_name or pokemon_base.get_name()
        self.__atks = sample(self.__poke.get_atk_list(),4) if len(self.__poke.get_atk_list())>4 else self.__poke.get_atk_list()
        self.__max_life = randint(self.__poke.get_life()[0],self.__poke.get_life()[1])
        self.__life = self.__max_life
        self.__effect: Effects.Base | None = None
        self.__next_act = Act('No act')
        pass
    def get_max_life(self):
        return self.__max_life
    def get_life(self):
        return self.__life
    def set_life(self,life:int):
        assert(isinstance(life,int))
        self.__life = 0 if life<=0 else life
    
    def get_type(self):
        return self.__poke.get_type()
    
    def get_name(self):
        return self.__name
    
    def get_attacks(self):
        return self.__atks
    
    def set_next_act(self,atk:Act|Attack):
        assert(isinstance(atk,Act) or isinstance(atk,Attack))
        self.__next_act = atk
    def get_next_act(self): return self.__next_act
    def execute_next_turn(self,pokemon_attacked:Pokemon):
        
        if isinstance(self.__effect,Effects.Base):
            can_atk, atk_proba = self.__effect.can_atk()
            if self.__effect.take_damage()[0]:
                self.__effect.take_damage()[0]
            self.__effect.end_effect()
            if can_atk and randint(0,100)<=atk_proba:
                if isinstance(self.__next_act,Attack):
                    self.__next_act.attack(pokemon_attacked,self)
                else:
                    self.__next_act.use(self)
            else:
                print(f'{self.get_name()} ne peut pas attaquer a cause de son effet: {self.__effect.get_name()}')
                
        else:
            if isinstance(self.__next_act,Attack):
                self.__next_act.attack(pokemon_attacked,self)
            else:
                self.__next_act.use(self)
        #print(f'{self.get_name()} ne peut pas attaquer a cause de son effet: {self.__effect.get_name()}')
        self.__next_act = Act('No act')

class Act:
    def __init__(self,name:str) -> None:
        assert(isinstance(name,str))
        self.__name = name
        
        pass
    def get_name(self): return self.__name
    def get_act_type(self) -> str|None: return None
    def get_priority(self) -> int: return 101 ## Because we want to do action after someone (100 = First, 0 = Last)
    def use(self,pokemon_that_beneficies:Pokemon):
        pass

class Attack_Scheme(Act):
    def __init__(self,name:str,typeatk:Pokemon_basics.types_type_def,damage:tuple[int,int],uses:tuple[int,int],priority:int,shock_itself:tuple[bool,tuple[int,int]|None]) -> None:
        super().__init__(name)
        assert(isinstance(name,str))
        assert(typeatk in Pokemon_basics.types)
        assert(isinstance(damage,tuple) and len(damage) == 2)
        assert(isinstance(uses,tuple) and len(uses)==2)
        assert(isinstance(priority,int) and priority in range(0,101))
        assert(isinstance(shock_itself,tuple))
        self.__shock_itself: list[bool|tuple[int,int]] = [shock_itself[0], shock_itself[1] if shock_itself[0] and isinstance(shock_itself[1],tuple) and len(shock_itself[1])==2 else (0,0)]
        self.__typeatk = typeatk
        self.__damage = damage
        self.__max_uses = (uses[0],uses[1])
        self.__priority = priority

        pass
    def get_type(self): return self.__typeatk
    def get_act_type(self): return 'atk'
    def get_shock_itself(self): return self.__shock_itself
    def get_priority(self): return self.__priority
    def get_uses_range(self):return self.__max_uses
    def set_uses(self,uses:int): self.__uses = uses

    def attack(self,pokemon_attacked:Pokemon,pokemon_that_attack:Pokemon,uses:Callable[[],None]):
        uses()
        #if pokemon_attacked.get_type()
        damage = randint(self.__damage[0],self.__damage[1])
        new_life = pokemon_attacked.get_life()-damage
        print(damage,new_life,pokemon_attacked.get_life())
        pokemon_attacked.set_life(new_life)
        return

class Attack:
    def __init__(self, attack_base:Attack_Scheme) -> None:
        assert(isinstance(attack_base,Attack_Scheme))
        self.__attack_scheme = attack_base
        self.__max_uses = randint(self.__attack_scheme.get_uses_range()[0],self.__attack_scheme.get_uses_range()[1])
        self.__uses = self.__max_uses

    def get_max_uses(self):return self.__max_uses
    def get_uses(self):return self.__uses
    def set_uses(self,uses:int): self.__uses = uses
    def use_one_use(self): self.__uses-=1
    def get_name(self):return self.__attack_scheme.get_name()
    def get_type(self):return self.__attack_scheme.get_type()
    def get_priority(self):return self.__attack_scheme.get_priority()
    def attack(self,pokemon_attacked:Pokemon,pokemon_that_attack:Pokemon):
        print(f'{pokemon_that_attack.get_name()} utilise {self.__attack_scheme.get_name()} !')
        return self.__attack_scheme.attack(pokemon_attacked,pokemon_that_attack,self.use_one_use)

