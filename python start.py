from tkinter import*
import time
import random
class Ball:
    def __init__(seft,canvas,color,van):
        seft.canvas = canvas
        seft.vando=van
        seft.id = canvas.create_oval(10,10,25,25,fill=color)
        seft.canvas.move(seft.id, 100, 200)
        start=[-3,-2,-1,1,2,3]
        random.shuffle(start)
        seft.x=start[0];
        seft.y=1;
        seft.canvas_height=500;
        seft.canvas_width=400;
        seft.over= False
    def vacham(seft,pos):
        pos_vando=seft.canvas.coords(seft.vando.id)
        if pos[0]>=pos_vando[0] and pos[0] <= pos_vando[2]:
            if pos[1]>= pos_vando[1] and pos[3]<=pos_vando[3]:
                return True
        return False
    def draw(seft):
        seft.canvas.move(seft.id, seft.x, seft.y)
        pos= seft.canvas.coords(seft.id)
        if pos[1]<=0:
            seft.y=2
        if pos[3] >= seft.canvas_height:
            seft.over= True
        if seft.vacham(pos)==True:
            seft.y=-2        
        if pos[0]<=0:
            seft.x=2;
        if pos[2] >= seft.canvas_width:
            seft.x= -2;
class vando:
    def __init__(seft,canvas,color):
        seft.canvas= canvas
        seft.id=canvas.create_rectangle(0,0,100,20,fill=color)
        seft.canvas.move(seft.id,300,400)
        seft.canvas.bind_all('<KeyPress-Left>',seft.trai)
        seft.canvas.bind_all('<KeyPress-Right>',seft.phai)
        seft.x=0;
        seft.y=0;
    def draw(seft):
        seft.canvas.move(seft.id,seft.x,seft.y)
    def trai(seft,event):
        seft.x=-2;
    def phai(seft,event):
        seft.x=2;
        
        
tk=Tk()
tk.title("game do bong")
tk.resizable(0,0)
can=Canvas(tk, width=400, height=500)
can.pack()
van=vando(can,"blue")
bong=Ball(can,"red",van)

while 1:
    if bong.over !=True:
        bong.draw()
        van.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    else:
        break;
print("game over")
