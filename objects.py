from pokemon import Pokemon, Act

class Objects:
    class Potion(Act):
        def __init__(self, name: str) -> None:
            super().__init__(name)
        def use(self, pokemon_that_beneficies: Pokemon):
            new_life = pokemon_that_beneficies.get_life()+60
            if new_life >= pokemon_that_beneficies.get_max_life():
                pokemon_that_beneficies.set_life(pokemon_that_beneficies.get_max_life())
            else:
                pokemon_that_beneficies.set_life(new_life)