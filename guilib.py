from typing import Literal
from pokemon import Attack, Pokemon
import pyxel


class GuiVar:
    class Pokemon:
        positions: dict[str, list[tuple[int, int, int]]] = {
            "salameche": [(0, 0, 0)],
            "bulbizare": [(32, 0, 0)],
            "carapuce": [(16, 0, 11)],
            "pikachu": [(48, 0, 7)],
            "magicarpe": [(64, 0, 0)],
            "chrysapile": [(80, 0, 0), (96, 0, 0)],
            "rattatac": [(112, 0, 0)],
            "ectoplasma": [(0, 16, 0)],
        }
        types = Literal["salameche", "bulbizare", "carapuce", "pikachu", "magicarpe", "chrysapile", "rattatac", "ectoplasma"]

    class Types:
        positions: dict[str, tuple[int, int, int]] = {"normal": (0, 8, 0), "fire": (8, 8, 0), "water": (16, 8, 0), "grass": (24, 8, 0), "electric": (32, 8, 0), "ghost": (40, 8, 0)}
        types = Literal["normal", "fire", "water", "grass", "electric", "ghost"]


class GuiLib:
    class BltUpscaler:
        def __init__(self, id: str, x: int, y: int, multiply: int, original_args: tuple[int, int, int, int, int, int]) -> None:
            assert isinstance(x, int) and isinstance(y, int)
            assert isinstance(multiply, int)
            self.id = id
            self.__x, self.__y, self.__multiply = x, y, multiply
            self.__original_args = (original_args[0], original_args[1], original_args[2], original_args[3], original_args[4], original_args[5])
            pass

        def draw(self):
            # pyxel.blt(self.__original_args[6],self.__original_args[7])
            dir = -1 if self.__original_args[3] <= 1 else 1
            for x in range(0, self.__original_args[3], dir):
                for y in range(self.__original_args[4]):
                    # pyxel.pset(self.__x+(x*self.__multiply),self.__y+(y*self.__multiply),7)
                    pyxel.blt(
                        self.__x + (x * self.__multiply),
                        self.__y + (y * self.__multiply),
                        self.__original_args[0],
                        self.__original_args[1] + abs(x),
                        self.__original_args[2] + y,
                        1,
                        1,
                        self.__original_args[5],
                    )
                    if pyxel.pget(self.__x + (x * self.__multiply), self.__y + (y * self.__multiply)) != self.__original_args[5]:
                        pyxel.rect(
                            self.__x + (x * self.__multiply),
                            self.__y + (y * self.__multiply),
                            self.__multiply,
                            self.__multiply,
                            pyxel.pget(self.__x + (x * self.__multiply), self.__y + (y * self.__multiply)),
                        )
                    # pyxel.rect(x,y,self.__multiply,self.__multiply,pyxel.pget(y,x))

    class Pokemon:
        def __init__(self, id: str, x: int, y: int, pokemon: GuiVar.Pokemon.types, flip: bool = False) -> None:
            assert isinstance(x, int) and isinstance(y, int)
            assert pokemon in list(GuiVar.Pokemon.positions.keys())
            assert isinstance(flip, bool)
            self.id = id
            self.__x, self.__y = x, y
            self.__zone = GuiVar.Pokemon.positions[pokemon][0]
            self.__flip: int = -16 if flip else 16
            pass

        def get_x(self):
            return self.__x

        def set_x(self, x: int):
            self.__x = x

        def get_y(self):
            return self.__y

        def draw(self):
            GuiLib.BltUpscaler(self.id, self.__x, self.__y, 2, (0, self.__zone[0], self.__zone[1], self.__flip, 16, self.__zone[2])).draw()
            pass

        def update(self):
            pass

    class PokemonStatus:
        def __init__(self, id: str, x: int, y: int, pokemon: Pokemon) -> None:
            assert isinstance(x, int) and isinstance(y, int)
            self.id = id
            self.__x, self.__y = x, y
            self.__poke = pokemon
            self.__life: list[int] = [self.__poke.get_life(), self.__poke.get_life()]
            self.__animation: tuple[bool, int, int, int] = (False, 0, 0, 0)
            pass

        def draw(self):
            # Background
            pyxel.blt(self.__x, self.__y, 1, 0, 0, 2, 2, 0)
            pyxel.blt(self.__x + 52, self.__y, 1, 2, 0, 2, 2, 0)
            pyxel.blt(self.__x, self.__y + 20, 1, 0, 2, 2, 2, 0)
            pyxel.blt(self.__x + 52, self.__y + 20, 1, 2, 2, 2, 2, 0)
            for i in range(1, 52):
                pyxel.blt(self.__x + i, self.__y, 1, 1, 0, 1, 2, 0)
                pyxel.blt(self.__x + i, self.__y + 20, 1, 2, 2, 1, 2, 0)
            for x in range(54):
                for y in range(2, 20):
                    pyxel.blt(self.__x + x, self.__y + y, 1, 1, 1, 1, 1, 0)

            # Pokemon
            pyxel.text(self.__x + 2, self.__y + 2, self.__poke.get_name(), 7)
            typecoords = GuiVar.Types.positions[self.__poke.get_type()]
            pyxel.blt(self.__x + 45, self.__y + 1, 1, typecoords[0], typecoords[1], 8, 8, typecoords[2])

            # Life Bar
            pyxel.rectb(self.__x + 2, self.__y + 9, 41, 5, 13)
            for x in [self.__x + 2, self.__x + 42]:
                for y in [self.__y + 9, self.__y + 13]:
                    pyxel.pset(x, y, 1)
            if self.__animation[0]:
                life_offset = ((self.__life[1] - self.__life[0]) / self.__animation[3]) * (pyxel.frame_count - self.__animation[1])
                # print((self.__life[1]-(self.__life[0]-self.__life[1]/self.__animation[3])*pyxel.frame_count-self.__animation[1]),self.__poke.get_max_life())
                pyxel.rect(self.__x + 3, self.__y + 10, int(((self.__life[1] - life_offset) / self.__poke.get_max_life()) * 39), 3, 8)
            else:
                pyxel.rect(self.__x + 3, self.__y + 10, int((self.__poke.get_life() / self.__poke.get_max_life()) * 39), 3, 8)
            # Life text
            if self.__animation[0]:
                life_offset = ((self.__life[1] - self.__life[0]) / self.__animation[3]) * (pyxel.frame_count - self.__animation[1])
                life_col = self.color_from_life((self.__life[1] - life_offset), self.__poke.get_max_life())
                pyxel.text(self.__x + 2, self.__y + 15, str(int(self.__life[1] - life_offset)), life_col)
            else:
                life_col = self.color_from_life(self.__poke.get_life(), self.__poke.get_max_life())
                pyxel.text(self.__x + 2, self.__y + 15, str(self.__poke.get_life()), life_col)

            pyxel.text(self.__x + 44 - (4 * len(str(self.__poke.get_max_life()))), self.__y + 15, str(self.__poke.get_max_life()), 7)
            pass

        def update(self):
            if self.__life[0] != self.__poke.get_life():
                self.__life[1] = self.__life[0]
                self.__life[0] = self.__poke.get_life()
                print(self.__life)
            if self.__animation[0] and self.__animation[2] < pyxel.frame_count:
                self.__animation = (False, self.__animation[1], self.__animation[2], self.__animation[3])
                self.__life = [self.__poke.get_life(), self.__poke.get_life()]
            pass

        def color_from_life(self, life: int | float, max_life: int):
            life_col: int
            life_percent = (life / max_life) * 100
            if life_percent <= 10:
                life_col = 8
            elif life_percent <= 30:
                life_col = 9
            elif life_percent <= 50:
                life_col = 10
            else:
                life_col = 7
            return life_col

        def animate_life(self, duration: int):
            self.__animation = (True, pyxel.frame_count, pyxel.frame_count + duration, duration)

    class Btn:
        def __init__(self, id: str, x: int, y: int, w: int, h: int, text: str, col: int) -> None:
            assert isinstance(x, int) & isinstance(y, int) & isinstance(w, int) & isinstance(h, int)
            assert isinstance(col, int)
            assert isinstance(text, str)
            # assert(len(text)*4<w & h<=6)
            self.id = id
            self.__text = text
            self.__x, self.__y, self.__w, self.__h = x, y, w, h
            self.__col = col
            self.__hover, self.__clicked = False, False
            pass

        def get_x(self):
            return self.__x

        def get_y(self):
            return self.__y

        def get_w(self):
            return self.__w

        def get_h(self):
            return self.__h

        def get_text(self):
            return self.__text

        def get_col(self):
            return self.__col

        def update(self):
            if self.__x < pyxel.mouse_x < self.__x + self.__w and self.__y < pyxel.mouse_y < self.__y + self.__h:
                self.__hover = True
            else:
                self.__hover = False
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if self.__x < pyxel.mouse_x < self.__x + self.__w and self.__y < pyxel.mouse_y < self.__y + self.__h:
                    self.__clicked = True
            pass

        def is_clicked(self, click_detect: bool):
            return self.__hover and click_detect

        def click_handled(self):
            self.__clicked = False

        def draw(self):
            if not self.__hover:
                ### Angles
                pyxel.blt(self.__x, self.__y, 1, 0, 0, 2, 2, 0)
                pyxel.blt(self.__x + self.__w - 2, self.__y, 1, 2, 0, 2, 2, 0)
                pyxel.blt(self.__x, self.__y + self.__h - 2, 1, 0, 2, 2, 2, 0)
                pyxel.blt(self.__x + self.__w - 2, self.__y + self.__h - 2, 1, 2, 2, 2, 2, 0)
                for i in range(1, self.__w - 2):
                    pyxel.blt(self.__x + i, self.__y, 1, 1, 0, 1, 2, 0)
                    pyxel.blt(self.__x + i, self.__y + self.__h - 2, 1, 2, 2, 1, 2, 0)
                for x in range(self.__w):
                    for y in range(2, self.__h - 2):
                        pyxel.blt(self.__x + x, self.__y + y, 1, 1, 1, 1, 1, 0)
            else:
                ### Angles
                pyxel.blt(self.__x, self.__y, 1, 4, 0, 2, 2, 0)
                pyxel.blt(self.__x + self.__w - 2, self.__y, 1, 6, 0, 2, 2, 0)
                pyxel.blt(self.__x, self.__y + self.__h - 2, 1, 4, 2, 2, 2, 0)
                pyxel.blt(self.__x + self.__w - 2, self.__y + self.__h - 2, 1, 6, 2, 2, 2, 0)
                for i in range(1, self.__w - 2):
                    pyxel.blt(self.__x + i, self.__y, 1, 5, 0, 1, 2, 0)
                    pyxel.blt(self.__x + i, self.__y + self.__h - 2, 1, 6, 2, 1, 2, 0)
                for x in range(self.__w):
                    for y in range(2, self.__h - 2):
                        pyxel.blt(self.__x + x, self.__y + y, 1, 5, 1, 1, 1, 0)
                pass
            self._draw_text()
            pass

        def _draw_text(self):
            y_text_pos = ((self.__h - 4) // 2) + self.__y
            x_text_pos = ((self.__w - len(self.__text) * 4) // 2) + self.__x
            pyxel.text(x_text_pos, y_text_pos, self.__text, self.__col)

    class AtkBtn(Btn):
        def __init__(self, id: str, x: int, y: int, w: int, h: int, atktxt: str, atkcol: int, usesnb: tuple[int, int], atktype: GuiVar.Types.types, atkvar: Attack) -> None:
            super().__init__(id, x, y, w, h, atktxt, atkcol)
            assert isinstance(usesnb, tuple)
            assert isinstance(usesnb[0], int) & isinstance(usesnb[1], int)
            assert atktype in list(GuiVar.Types.positions.keys())
            assert isinstance(atkvar, Attack)
            self.__uses_nb = usesnb
            self.__type = atktype
            self.atk = atkvar

        def _draw_text(self):
            # Atk name
            pyxel.text(self.get_x() + 2, self.get_y() + 2, self.get_text(), self.get_col())
            # Atk uses
            uses_col = 8 if self.__uses_nb[0] <= 2 else 7
            pyxel.text(self.get_x() + 2, self.get_y() + self.get_h() - 8, f"Uses:{self.__uses_nb[0]}/{self.__uses_nb[1]}", uses_col)
            pyxel.blt(
                self.get_x() + self.get_w() - 10,
                self.get_y() + (self.get_h() // 2) - 4,
                1,
                GuiVar.Types.positions[self.__type][0],
                GuiVar.Types.positions[self.__type][1],
                8,
                8,
                GuiVar.Types.positions[self.__type][2],
            )
            # pyxel.text(self.get_x()+2,self.get_y()+2,self.get_text(),self.get_col())

    class ReturnBtn(Btn):
        def __init__(self, id: str, x: int, y: int) -> None:
            super().__init__(id, x, y, 8, 8, "", 7)

        def draw(self):
            super().draw()
            pyxel.rect(self.get_x() + 2, self.get_y() + 2, 4, 1, 7)

    class Txt:
        def __init__(self, x: int, y: int, txt: str, col: int) -> None:
            assert isinstance(x, int) and isinstance(y, int) and isinstance(txt, str) and isinstance(col, int)
            self.__x, self.__y, self.__txt, self.__col = x, y, txt, col
            pass

        def update(self):
            pass

        def draw(self):
            pyxel.text(self.__x, self.__y, self.__txt, self.__col)
