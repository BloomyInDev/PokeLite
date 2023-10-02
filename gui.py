import pyxel
from guilib import GuiLib
class Game:
    def __init__(self) -> None:
        pyxel.init(128,160)
        pyxel.mouse(True)
        pyxel.load('./ressources.pyres')
        self.__whereiam = 'home'
        self.__btn: list[GuiLib.Btn] = [GuiLib.Btn(2,50,50,9,'Coucou',12,6,7),GuiLib.Btn(2,70,50,11,'Coucou2',12,6,7)]
        
        
        pyxel.run(self.update,self.draw)
        pass
    def update(self) -> None:
        pass
    def draw(self) -> None:
        pyxel.cls(0)
        pyxel.rect(0,1,26*4,6,5)
        pyxel.text(0,1,'abcdefghijklmnopqrstuvwxyz',10)
        pyxel.text(0,10,'ABCDEFGHIJKLMNOPQRSTUVWXYZ',10)
        self.__btn[0].draw()
        self.__btn[1].draw()
        match self.__whereiam:
            case 'home':
                pass
            case _:
                pyxel.cls(5)
        pass
    
Game()