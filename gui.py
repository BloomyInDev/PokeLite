import pyxel
from guilib import GuiLib
class Game:
    def __init__(self) -> None:
        pyxel.init(128,160,fps=60)
        pyxel.mouse(True)
        pyxel.load('./ressources.pyxres')
        self.__whereiam = 'home'
        self.__btn: list[GuiLib.Btn] = [
            GuiLib.Btn(3,116,60,20,'Attaquer',7),
            GuiLib.Btn(65,116,60,20,'Attaquer',7),
            GuiLib.Btn(3,138,60,20,'Attaquer',7),
            GuiLib.Btn(65,138,60,20,'Attaquer',7),
            GuiLib.AtkBtn(3,90,60,20,'Morsure',7,(3,10),'Normal',7)
        ]
        self.__poke: list[GuiLib.Pokemon] = [
            GuiLib.Pokemon(3,70,'carapuce'),
            GuiLib.Pokemon(33,70,'bulbizare')
        ]
        
        
        pyxel.run(self.update,self.draw)
        pass
    def update(self) -> None:
        for btn in self.__btn:
            btn.update()
        pass
    def draw(self) -> None:
        pyxel.cls(0)
        pyxel.rect(0,1,26*4,6,5)
        pyxel.text(0,1,'abcdefghijklmnopqrstuvwxyz',10)
        pyxel.text(0,10,'ABCDEFGHIJKLMNOPQRSTUVWXYZ',10)
        for btn in self.__btn:
            btn.draw()
        for poke in self.__poke:
            poke.draw()
        match self.__whereiam:
            case 'home':
                pass
            case _:
                pyxel.cls(5)
        pass
    
Game()