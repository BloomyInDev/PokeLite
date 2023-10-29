import pyxel
from guilib import GuiLib
from arena import Arena
pokerandom = Arena().choose_random_poke()
class Game:
    def __init__(self) -> None:
        pyxel.init(128,100,fps=60)
        pyxel.mouse(True)
        pyxel.load('./ressources.pyxres')
        self.__whereiam = 'home'
        self.__ui = [
            GuiLib.Btn(3,56,60,20,'Attaquer',7),
            GuiLib.Btn(65,56,60,20,'Objets',7),
            GuiLib.Btn(3,78,60,20,'Pokemon',7),
            GuiLib.Btn(65,78,60,20,'Fuir',7),
            #GuiLib.AtkBtn(3,30,60,20,'Morsure',7,(2,10),'normal'),
            GuiLib.Pokemon(3,30,pokerandom.get_id()),
            GuiLib.Pokemon(33,30,pokerandom.get_id(),True),
            GuiLib.PokemonStatus(3,2,pokerandom)
        ]
        pyxel.run(self.update,self.draw)
        pass
    def update(self) -> None:
        for uie in self.__ui:
            uie.update()
        pass
    def draw(self) -> None:
        pyxel.cls(0)
        #pyxel.rect(0,1,26*4,6,5)
        #pyxel.text(0,1,'abcdefghijklmnopqrstuvwxyz',10)
        #pyxel.text(0,10,'ABCDEFGHIJKLMNOPQRSTUVWXYZ',10)
        for uie in self.__ui:
            uie.draw()
        #match self.__whereiam:
        #    case 'home':
        #        pass
        #    case _:
        #        pyxel.cls(5)
        pass
    
Game()