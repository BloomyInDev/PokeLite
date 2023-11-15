from pokemon import Pokemon


class Player:
    def __init__(self, name: str, deck: list[Pokemon]) -> None:
        assert isinstance(name, str)
        assert type(deck) == list and len(deck) > 0
        for poke in deck:
            assert isinstance(poke, Pokemon)
        self.name: str = name
        self.__deck: list[Pokemon] = deck
        self.__pokemon_out: Pokemon = deck[0]
        pass

    def get_deck(self):
        return self.__deck

    def get_poke_out(self):
        return self.__pokemon_out

    def change_poke_out(self, i: int):
        self.__pokemon_out = self.__deck[i]
