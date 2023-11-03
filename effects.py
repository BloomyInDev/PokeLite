class Effect_Default:
    def __init__(self, name: str, can_atk: bool, atk_proba: int, take_damage: bool, damage_val: int, end_effect: int) -> None:
        assert isinstance(name, str)
        self.__name = name
        assert isinstance(can_atk, bool)
        self.__can_atk = can_atk
        assert isinstance(atk_proba, int)
        self.__atk_proba = atk_proba
        assert isinstance(take_damage, bool)
        self.__take_damage = take_damage
        assert isinstance(damage_val, int)
        self.__damage_val = damage_val
        assert isinstance(end_effect, int)
        self.__end_effect = end_effect
        pass

    def get_name(self):
        return self.__name

    def can_atk(self) -> tuple[bool, int]:
        return self.__can_atk, self.__atk_proba

    def take_damage(self) -> tuple[bool, int]:
        return self.__take_damage, self.__damage_val

    def end_effect(self) -> int | bool:
        return self.__end_effect if self.__end_effect != -1 else False

    def reduce_effect_duration(self):
        self.__end_effect -= 1


class Effects:
    class Base:
        def __init__(self) -> None:
            self.e = Effect_Default("Default", False, 0, False, 0, 7)
            pass

        def get_name(self):
            return self.e.get_name()

        def can_atk(self):
            return self.e.can_atk()

        def take_damage(self):
            return self.e.take_damage()

        def end_effect(self):
            return self.e.end_effect()

        def reduce_effect_duration(self):
            return self.e.reduce_effect_duration()

    class Sleep(Base):
        def __init__(self) -> None:
            self.e = Effect_Default("Endormi", False, 0, False, 0, 7)

    class Burn(Base):
        def __init__(self) -> None:
            self.e = Effect_Default("Brulure", True, 50, True, 10, -1)
