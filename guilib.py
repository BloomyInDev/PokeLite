import pyxel
class GuiLib:
    class Btn:
        def __init__(self,x:int,y:int,w:int,h:int,text:str,col:int,colh:int,colt:int) -> None:
            assert(isinstance(x,int)&isinstance(y,int)&isinstance(w,int)&isinstance(h,int))
            assert(isinstance(col,int)&isinstance(colh,int)&isinstance(colt,int))
            assert(isinstance(text,str))
            #assert(len(text)*4<w & h<=6)
            self.__text = text
            self.__x,self.__y,self.__w,self.__h= x, y, w, h
            self.__col,self.__colh, self.__colt = col,colh,colt
            pass
        def draw(self):
            y_text_pos = ((self.__h-4)//2)+self.__y
            pyxel.rect(self.__x,self.__y,self.__w,self.__h,self.__col)
            pyxel.text(self.__x,y_text_pos,self.__text,self.__colt)
            pass