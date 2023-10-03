from pokemon import Pokemon_basics
from typing import Literal
import pyxel
class GuiCfg:
    class Pokemon:
        positions: dict[str, list[tuple[int,int,int]]] = {
            "salameche":[(0,0,0)],
            "bulbizare":[(32,0,0)],
            "carapuce":[(16,0,11)],
            "pikachu":[(48,0,7)],
            "magicarpe":[(64,0,0)],
            "chrysapile":[(80,0,0),(96,0,0)],
            "rattatac":[(112,0,0)],
            "ectoplasma":[(0,16,0)]
        }
        types = Literal["salameche","bulbizare","carapuce","pikachu","magicarpe","chrysapile","rattatac","ectoplasma"]
class GuiLib:
    class Pokemon:
        def __init__(self,x:int,y:int,pokemon:GuiCfg.Pokemon.types) -> None:
            assert(isinstance(x,int) and isinstance(y,int))
            assert(pokemon in list(GuiCfg.Pokemon.positions.keys()))
            self.__x, self.__y = x, y
            self.__zone = GuiCfg.Pokemon.positions[pokemon][0]
            pass
        def draw(self):
            pyxel.blt(self.__x,self.__y,0,self.__zone[0],self.__zone[1],16,16,self.__zone[2])
            pass
    class Btn:
        def __init__(self,x:int,y:int,w:int,h:int,text:str,col:int) -> None:
            assert(isinstance(x,int) & isinstance(y,int) & isinstance(w,int) & isinstance(h,int))
            assert(isinstance(col,int))
            assert(isinstance(text,str))
            #assert(len(text)*4<w & h<=6)
            self.__text = text
            self.__x,self.__y,self.__w,self.__h= x, y, w, h
            self.__col = col
            self.__hover = False
            pass
        def get_x(self): return self.__x
        def get_y(self): return self.__y
        def get_w(self): return self.__w
        def get_h(self): return self.__h
        def get_text(self): return self.__text
        def get_col(self): return self.__col
        def update(self):
            if (self.__x < pyxel.mouse_x < self.__x+self.__w and self.__y < pyxel.mouse_y < self.__y+self.__h): self.__hover = True
            else: self.__hover = False
            pass
        def draw(self):
            
            if not self.__hover:
                ### Angles
                pyxel.blt(self.__x           ,self.__y           ,1,0,0,2,2,0)
                pyxel.blt(self.__x+self.__w-2,self.__y           ,1,2,0,2,2,0)
                pyxel.blt(self.__x           ,self.__y+self.__h-2,1,0,2,2,2,0)
                pyxel.blt(self.__x+self.__w-2,self.__y+self.__h-2,1,2,2,2,2,0)
                for i in range(1,self.__w-2):
                    pyxel.blt(self.__x+i,self.__y,1,1,0,1,2,0)
                    pyxel.blt(self.__x+i,self.__y+self.__h-2,1,2,2,1,2,0)
                for x in range(self.__w):
                    for y in range(2,self.__h-2):
                        pyxel.blt(self.__x+x,self.__y+y,1,1,1,1,1,0)
            else:
                ### Angles
                pyxel.blt(self.__x           ,self.__y           ,1,4,0,2,2,0)
                pyxel.blt(self.__x+self.__w-2,self.__y           ,1,6,0,2,2,0)
                pyxel.blt(self.__x           ,self.__y+self.__h-2,1,4,2,2,2,0)
                pyxel.blt(self.__x+self.__w-2,self.__y+self.__h-2,1,6,2,2,2,0)
                for i in range(1,self.__w-2):
                    pyxel.blt(self.__x+i,self.__y,1,5,0,1,2,0)
                    pyxel.blt(self.__x+i,self.__y+self.__h-2,1,6,2,1,2,0)
                for x in range(self.__w):
                    for y in range(2,self.__h-2):
                        pyxel.blt(self.__x+x,self.__y+y,1,5,1,1,1,0)
                pass
            self._draw_text()
            pass
        def _draw_text(self):
            y_text_pos = ((self.__h-4)//2)+self.__y
            x_text_pos = ((self.__w-len(self.__text)*4)//2)+self.__x
            pyxel.text(x_text_pos,y_text_pos,self.__text,self.__col)
    class AtkBtn(Btn):
        def __init__(self, x: int, y: int, w: int, h: int, atktxt: str, atkcol: int, usesnb: tuple[int,int], typetxt: str, typecol: int) -> None:
            super().__init__(x, y, w, h, atktxt, atkcol)
            assert(isinstance(usesnb,tuple))
            assert(isinstance(usesnb[0],int) & isinstance(usesnb[1],int))
            assert(isinstance(typecol,int) & isinstance(typetxt,str))
            self.__uses_nb = usesnb
            self.__type_col, self.__type_txt = typecol, typetxt
        def _draw_text(self):
            # Atk name
            pyxel.text(self.get_x()+2,self.get_y()+2,self.get_text(),self.get_col())
            # Atk uses
            uses_col = 8 if self.__uses_nb[0]<=2 else 7
            pyxel.text(self.get_x()+2,self.get_y()+self.get_h()-8,f'Uses:{self.__uses_nb[0]}/{self.__uses_nb[1]}',uses_col)
            #pyxel.text(self.get_x()+2,self.get_y()+2,self.get_text(),self.get_col())