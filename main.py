# -*- coding: utf-8 -*-
from tkinter import *
import time

main = Tk()

getspawn = Tk()
getspawn.geometry("150x150")
getspawn.resizable(False, False)
getdot = Tk()
getdot.geometry("150x150")
getdot.resizable(False, False)

moves = 0
screenx = main.winfo_screenwidth()
screenz = main.winfo_screenheight()

canvas = Canvas(main, width = screenx, height = screenz, bg = "#2d2d33")
canvas.pack(expand=1)

def motion(event):
    global dotxz
    if dotxz[0] % 1 == 0:
        x, z = event.x - int(screenx/2), event.y - int(screenz/2)
        global moves
        if moves % 500 == 0:
            print('\nКоординаты мыши за последние 500 движений: {}, {}'.format(0+dotxz[0] + x, 0+dotxz[1] + -z))
            print("\nx на программном уровне:", x,
                  "\nz на программном уровне:", z,
                  "\nscreenz:", screenz,
                  "\nscreenx:", screenx)        
            moves = 0
        cursorxy.place(x=x+screenx/2+10, y=z+screenz/2+10)
        cursorxy["text"] = 0+dotxz[0] + x, 0+dotxz[1] + -z
        moves+=1
    
hub = Entry(getspawn, relief = FLAT)
hub.pack()

def spawn():
    global dotxz
    print(hub.get())
    dotxz = str(hub.get())
    dotxz = dotxz.split(" ")
    dotxz[0] = int(dotxz[0])
    dotxz[1] = int(dotxz[1])
    canvas.create_line(screenx/2-1000, screenz/2, screenx/2, screenz/2, width = 3, fill = "red")
    canvas.create_line(screenx/2, screenz/2-1000, screenx/2, screenz/2, width = 3, fill = "blue")
    canvas.create_line(screenx/2, screenz/2, screenx/2+1000, screenz/2, width = 3, fill = "green")
    canvas.create_line(screenx/2, screenz/2, screenx/2, screenz/2+500, width = 3, fill = "white")
    canvas.create_oval(-5+screenx/2, -5+screenz/2, 5+screenx/2, 5+screenz/2, fill = "#8A2BE2")   
    getspawn.destroy()
getspawnbut = Button(getspawn, text = "Спавн", relief = FLAT, command = spawn).pack()
cursorxy = Label(text = "", fg = "white", bg = "#2d2d33")


main.bind('<Motion>', motion)


print(screenx, screenz)
main.mainloop()
getspawn.mainloop()
