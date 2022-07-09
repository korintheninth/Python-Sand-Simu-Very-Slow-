import time
import pygame as pyg
import keyboard
import pyautogui as ptg

black = [0,0,0]
pyg.init
window = pyg.display.set_mode((0, 0), pyg.FULLSCREEN)
window.fill(black)
pyg.draw.rect(window, [149,138,138], pyg.Rect(0,1060,1920,20))
CURRENT=[]

velocity = 59.880239520958083832335329341317
FPS = 1.0
accel = 0.0
deltatime = 0.0167


def Spawn(): #boşluğa bastığında mousun pozisyonunu x,y halinde tupl olarak listeye ekliyor
    global timer
    mouse_pos = ptg.position() 
    if keyboard.is_pressed(" "):
       
        CURRENT.append((mouse_pos.x,mouse_pos.y))
        timer = 0.01

        
def Draw(): #currentdaki pozisyonlara 1 pixellik kare çiziyor

    window.fill(black)
    pyg.draw.rect(window, [149,138,138], pyg.Rect(0,1060,1920,20))
    for (x,y) in CURRENT:
        posx = x
        posy = y
        pyg.draw.rect(window, [255,128,0], pyg.Rect(posx,posy,1,1))


def Calculate():    #currentdaki pozisyonlara hız değerini ekleyip sonraki pozisyonlarını hesaplıyor ve bu pozisyonları currenta koyuyor eskilerini siliyor
    global deltatime
    #accel = 1 / FPS
    #velocity += accel
    for i in range(0,len(CURRENT)):
        x = CURRENT[i][0]
        y = CURRENT[i][1]

        nextPosy = y + 1
        nextPosx = x
        if nextPosy > 1060:
            nextPosy = 1060
            nextPosx = x
        elif CURRENT.count((nextPosx,nextPosy)) == 0:
            pass
        elif CURRENT.count((nextPosx + 1,nextPosy)) == 0:
            nextPosx = x+1
            nextPosy = y+1
        elif CURRENT.count((nextPosx - 1,nextPosy)) == 0:
            nextPosx = x-1
            nextPosy = y+1
        else: 
            nextPosx = x
            nextPosy = y

        nextPos = (nextPosx,nextPosy)
        CURRENT[i] = nextPos

while True:
    start_time = time.time()
    Spawn()
    Draw()
    pyg.display.update()
    Calculate()
    


    time.sleep(0.0000000000000000000001) #0'a bölümü engellemek için
    if keyboard.is_pressed("escape"):
        break
    end_time = time.time()
    deltatime = end_time - start_time
    FPS = 1.0 / (deltatime)
pyg.display.quit



    
    
