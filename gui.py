from typing import Literal
import pyxel
from guilib import GuiLib
from arena import Arena, DeckInitializer
from player import Player


class Game:
    def __init__(self) -> None:
        pyxel.init(128, 102, fps=60, title="PokeLite")
        pyxel.mouse(True)
        pyxel.load("./ressources.pyxres")
        self.__p1, self.__p2 = Player("Joueur 1", DeckInitializer().random(2)), Player("Joueur 2", DeckInitializer().random(2))
        # self.__p1, self.__p2 = Arena().choose_random_poke(), Arena().choose_random_poke()
        self.__round, self.__last_interact = 0, 0
        self.__player_playing = Arena().what_is_the_player_that_plays(self.__round, self.__p1, self.__p2)
        self.__player_not_playing = Arena().what_is_the_player_that_isnt_playing(self.__round, self.__p1, self.__p2)
        self.__where_i_am: Literal["home", "settings", "game-choose-action", "game-choose-atk", "game-choose-obj", "game-choose-poke", "game-action", "game-end"] = "game-choose-action"
        self.__action_start_end: tuple[int, int] = (0, 0)
        self.__p1_x_pos, self.__p2_x_pos = 3, 122
        self.__ui: dict[str, GuiLib.Btn | GuiLib.Pokemon | GuiLib.PokemonStatus | GuiLib.Txt | None] = {
            "atk_btn": GuiLib.Btn("atk_btn", 3, 58, 60, 20, "Attaquer", 7),
            "obj_btn": GuiLib.Btn("obj_btn", 65, 58, 60, 20, "Objets", 7),
            "poke_btn": GuiLib.Btn("poke_btn", 3, 80, 60, 20, "Pokemon", 7),
            "leave_btn": GuiLib.Btn("leave_btn", 65, 80, 60, 20, "Fuir", 7),
            "p1_poke": GuiLib.Pokemon("p1_poke", self.__p1_x_pos, 23, self.__p1.get_poke_out().get_id()),  # type: ignore # Need this cuz my IDE is mad else
            "p2_poke": GuiLib.Pokemon("p2_poke", self.__p2_x_pos, 23, self.__p2.get_poke_out().get_id(), True),  # type: ignore # Same as line before
            "p1_stat": GuiLib.PokemonStatus("p1_stat", 3, 2, self.__p1.get_poke_out()),
            "p2_stat": GuiLib.PokemonStatus("p1_stat", 71, 2, self.__p2.get_poke_out()),
        }
        pyxel.run(self.update, self.draw)
        pass

    def update(self) -> None:
        self.update_players()
        if self.__where_i_am == "game-action":
            if pyxel.frame_count > self.__action_start_end[1]:
                self.__action_start_end = (pyxel.frame_count, pyxel.frame_count + 105)
            if pyxel.frame_count <= self.__action_start_end[0] + 90:
                if ((self.__round % 2) + 1) == 1:
                    if pyxel.frame_count <= self.__action_start_end[0] + 45:
                        self.__p1_x_pos += 1
                    else:
                        self.__p1_x_pos -= 1
                else:
                    if pyxel.frame_count <= self.__action_start_end[0] + 45:
                        self.__p2_x_pos -= 1
                    else:
                        self.__p2_x_pos += 1
                # print('doing something')
            if pyxel.frame_count == self.__action_start_end[0] + 45:
                print("Now animating life")
                self.__player_playing.execute_next_turn(self.__player_not_playing)
                for e in ["p1_stat", "p2_stat"]:
                    uie = self.__ui[e]
                    assert isinstance(uie, GuiLib.PokemonStatus)
                    uie.animate_life(60)
            if pyxel.frame_count == self.__action_start_end[1]:
                self.__round += 1
                if self.__p1.get_poke_out().is_alive() and self.__p2.get_poke_out().is_alive():
                    self.__where_i_am = "game-choose-action"
                    self.__ui = self.__ui | {
                        "atk_btn": GuiLib.Btn("atk_btn", 3, 58, 60, 20, "Attaquer", 7),
                        "obj_btn": GuiLib.Btn("obj_btn", 65, 58, 60, 20, "Objets", 7),
                        "poke_btn": GuiLib.Btn("poke_btn", 3, 80, 60, 20, "Pokemon", 7),
                        "leave_btn": GuiLib.Btn("leave_btn", 65, 80, 60, 20, "Fuir", 7),
                    }
                else:
                    self.__where_i_am = "game-end"
                    txt_end = [f"{self.__player_not_playing.get_name()} est mort", f"Joueur {'1' if self.__p1.get_poke_out() == self.__player_playing else '2'} a gagne"]
                    self.__ui = self.__ui | {
                        "msg1-end": GuiLib.Txt((128 - (len(txt_end[0]) * 4)) // 2, 75, txt_end[0], 7),
                        "msg2-end": GuiLib.Txt((128 - (len(txt_end[1]) * 4)) // 2, 82, txt_end[1], 7),
                    }
        i = 0
        while i < len(self.__ui.keys()):
            pass_to_next_i: bool = True
            mouse_click = pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
            uie = self.__ui[list(self.__ui.keys())[i]]
            if uie != None:
                uie.update()
                if isinstance(uie, GuiLib.Btn):
                    if uie.is_clicked(mouse_click):
                        if self.__last_interact + 10 < pyxel.frame_count:
                            self.__last_interact = pyxel.frame_count
                            match self.__where_i_am:
                                case "home":
                                    print("in home")
                                case "game-choose-action":
                                    match uie.id:
                                        case "atk_btn":
                                            pass_to_next_i = False
                                            for e in ["atk_btn", "obj_btn", "poke_btn", "leave_btn"]:
                                                self.__ui.pop(e)
                                            for i, attack in enumerate(self.__player_playing.get_attacks()):
                                                x = 3 + (62 * (i % 2))
                                                y = 58 + (22 * (i // 2))
                                                self.__ui[f"atk{i+1}_atk_btn"] = GuiLib.AtkBtn(f"atk{i+1}_atk_btn", x, y, 60, 20, attack.get_name(), 7, (attack.get_uses(), attack.get_max_uses()), attack.get_type(), attack)  # type: ignore
                                            print(self.__player_playing.get_attacks())
                                            self.__where_i_am = "game-choose-atk"
                                        case "obj_btn":
                                            pass_to_next_i = False
                                            for e in ["atk_btn", "obj_btn", "poke_btn", "leave_btn"]:
                                                self.__ui.pop(e)
                                            self.__ui["return_btn"] = GuiLib.ReturnBtn("return_btn", 58, 75)
                                            self.__where_i_am = "game-choose-obj"
                                        case "poke_btn":
                                            pass_to_next_i = False
                                            for e in ["atk_btn", "obj_btn", "poke_btn", "leave_btn"]:
                                                self.__ui.pop(e)
                                            self.__ui["return_btn"] = GuiLib.ReturnBtn("return_btn", 58, 75)
                                            self.__where_i_am = "game-choose-poke"
                                        case "leave_btn":
                                            pass_to_next_i = False
                                            for e in ["atk_btn", "obj_btn", "poke_btn", "leave_btn"]:
                                                self.__ui.pop(e)
                                            txt_loose = f"Vous abandonez, Joueur {(self.__round%2)+1} a perdu !"
                                            self.__ui["loose_msg"] = GuiLib.Txt((128 - (len(txt_loose) * 4)) // 2, 75, txt_loose, 7)
                                        case _:
                                            pass
                                case "game-choose-atk":
                                    if uie.id in ["atk1_atk_btn", "atk2_atk_btn", "atk3_atk_btn", "atk4_atk_btn"]:
                                        assert isinstance(uie, GuiLib.AtkBtn)
                                        pass_to_next_i = False
                                        self.__player_playing.set_next_act(uie.atk)
                                        for e in ["atk1_atk_btn", "atk2_atk_btn", "atk3_atk_btn", "atk4_atk_btn"]:
                                            if e in list(self.__ui.keys()):
                                                self.__ui.pop(e)
                                        self.__where_i_am = "game-action"
                                case "game-choose-obj":
                                    if uie.id == "return_btn":
                                        self.__ui.pop("return_btn")
                                        self.__ui = self.__ui | {
                                            "atk_btn": GuiLib.Btn("atk_btn", 3, 58, 60, 20, "Attaquer", 7),
                                            "obj_btn": GuiLib.Btn("obj_btn", 65, 58, 60, 20, "Objets", 7),
                                            "poke_btn": GuiLib.Btn("poke_btn", 3, 80, 60, 20, "Pokemon", 7),
                                            "leave_btn": GuiLib.Btn("leave_btn", 65, 80, 60, 20, "Fuir", 7),
                                        }
                                        self.__where_i_am = "game-choose-action"
                                case "game-choose-poke":
                                    if uie.id == "return_btn":
                                        self.__ui.pop("return_btn")
                                        self.__ui = self.__ui | {
                                            "atk_btn": GuiLib.Btn("atk_btn", 3, 58, 60, 20, "Attaquer", 7),
                                            "obj_btn": GuiLib.Btn("obj_btn", 65, 58, 60, 20, "Objets", 7),
                                            "poke_btn": GuiLib.Btn("poke_btn", 3, 80, 60, 20, "Pokemon", 7),
                                            "leave_btn": GuiLib.Btn("leave_btn", 65, 80, 60, 20, "Fuir", 7),
                                        }
                                        self.__where_i_am = "game-choose-action"
                                case _:
                                    print(f"idk where i am\nHere the data:{self.__where_i_am},{uie}")
                            # print(f'{uie.id} has been clicked')
                            uie.click_handled()
                elif isinstance(uie, GuiLib.Pokemon):
                    match list(self.__ui.keys())[i]:
                        case "p1_poke":
                            uie.set_x(self.__p1_x_pos)
                        case "p2_poke":
                            uie.set_x(self.__p2_x_pos)
                        case _:  # Should not go here, it's to make my IDE happy
                            pass
            if pass_to_next_i:
                i += 1
        pass

    def draw(self) -> None:
        pyxel.cls(0)
        # pyxel.rect(0,1,26*4,6,5)
        # pyxel.text(0,1,'abcdefghijklmnopqrstuvwxyz',10)
        # pyxel.text(0,10,'ABCDEFGHIJKLMNOPQRSTUVWXYZ',10)
        pyxel.rect(0, 55, 128, 1, 3)
        pyxel.rect(0, 56, 128, 100, 11)
        if self.__where_i_am != "game-action":
            pyxel.text(60, 5, f"J{(self.__round%2)+1}", 7)
        for e in self.__ui.keys():
            uie = self.__ui[e]
            if uie != None:
                uie.draw()
        # match self.__whereiam:
        #    case 'home':
        #        pass
        #    case _:
        #        pyxel.cls(5)
        pass

    def update_players(self):
        self.__player_playing = Arena().what_is_the_player_that_plays(self.__round, self.__p1, self.__p2)
        self.__player_not_playing = Arena().what_is_the_player_that_isnt_playing(self.__round, self.__p1, self.__p2)


Game()
