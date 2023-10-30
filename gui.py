import pyxel
from guilib import GuiLib
from arena import Arena
p1, p2 = Arena().choose_random_poke(), Arena().choose_random_poke()
class Game:
    def __init__(self) -> None:
        pyxel.init(128,102,fps=60)
        pyxel.mouse(True)
        pyxel.load('./ressources.pyxres')
        self.__whereiam = 'home'
        self.__ui = [
            GuiLib.Btn(3,58,60,20,'Attaquer',7),
            GuiLib.Btn(65,58,60,20,'Objets',7),
            GuiLib.Btn(3,80,60,20,'Pokemon',7),
            GuiLib.Btn(65,80,60,20,'Fuir',7),
            #GuiLib.AtkBtn(3,30,60,20,'Morsure',7,(2,10),'normal'),
            GuiLib.Pokemon(3,23,p1.get_id()),
            GuiLib.Pokemon(122,23,p2.get_id(),True),
            GuiLib.PokemonStatus(3,2,p1),
            GuiLib.PokemonStatus(71,2,p2)
        ]
        pyxel.run(self.update,self.draw)
        pass
    def update(self) -> None:
        if pyxel.frame_count%10 == 0:
            p1.set_life(p1.get_life()-1)
            p2.set_life(p2.get_life()-1)
        for uie in self.__ui:
            uie.update()
        pass
    def draw(self) -> None:
        pyxel.cls(0)
        #pyxel.rect(0,1,26*4,6,5)
        #pyxel.text(0,1,'abcdefghijklmnopqrstuvwxyz',10)
        #pyxel.text(0,10,'ABCDEFGHIJKLMNOPQRSTUVWXYZ',10)
        pyxel.rect(0,55,128,1,3)
        pyxel.rect(0,56,128,100,11)
        for uie in self.__ui:
            uie.draw()
        #match self.__whereiam:
        #    case 'home':
        #        pass
        #    case _:
        #        pyxel.cls(5)
        pass
    
Game()