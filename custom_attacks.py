from effects import Effects
from pokemon import Attack_Scheme, Pokemon, Pokemon_basics
from random import randint

class Custom_Attack:
    class Half_Life_Damage_Attack(Attack_Scheme):
        def __init__(self, name: str, typeatk: Pokemon_basics.types_type_def, uses: tuple[int, int], priority: int, shock_itself: tuple[bool, tuple[int, int] | None]) -> None:
            super().__init__(name, typeatk, (1,1), uses, priority, shock_itself)
        def attack(self, pokemon_attacked:Pokemon, pokemon_that_attack:Pokemon,uses:function):
            assert(isinstance(pokemon_attacked,Pokemon))
            assert(isinstance(pokemon_that_attack,Pokemon))
            uses() # type:ignore
            new_life = pokemon_attacked.get_life()//2
            pokemon_attacked.set_life(new_life)
            if self.get_shock_itself()[0]:
                shock_itself_damage: tuple[int, int] = self.get_shock_itself()[1] # type: ignore
                new_life = pokemon_that_attack.get_life()-randint(shock_itself_damage[0],shock_itself_damage[1])
                pokemon_that_attack.set_life(new_life)
            return
    class Attack_With_Effect(Attack_Scheme):
        def __init__(self, name: str, typeatk: Pokemon_basics.types_type_def, damage: tuple[int, int], uses: tuple[int, int], priority: int, shock_itself: tuple[bool, tuple[int, int] | None],effect:Effects.Base) -> None:
            super().__init__(name, typeatk, damage, uses, priority, shock_itself)
            assert(isinstance(effect,Effects.Base))
            self.__effect = effect

        def attack(self, pokemon_attacked: Pokemon, pokemon_that_attack: Pokemon, uses:function):

            super().attack(pokemon_attacked, pokemon_that_attack,uses)