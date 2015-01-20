import pygame, sys, random, time, pygame.mixer, pygame.font
from pygame.locals import *
from pygame.font import *

from KeyInput import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 450

pygame.font.init()
myFont = pygame.font.SysFont("Comic Sans", 40)
myFont2 = pygame.font.SysFont("Comic Sans", 12)

nameinput= pygame.image.load('Images/Name Input.png')
cselect = pygame.image.load('Images/ColorSelect.png')
background = pygame.image.load('Images/gamebg.png')

red1 = pygame.image.load('Images/reds.png')
blue1 = pygame.image.load('Images/blues.png')
green1 = pygame.image.load('Images/greens.png')

red2 = pygame.image.load('Images/redp.png')
blue2 = pygame.image.load('Images/bluep.png')
green2 = pygame.image.load('Images/greenp.png')

size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(size)

playername = ""
counter = 0
KI = KeyInput('a')

while True:
    counter = counter + 1
    screen.blit(nameinput, (0,0))
    key = pygame.key.get_pressed()

    if key[K_ESCAPE]:
        sys.exit()
        
    elif key[K_BACKSPACE]:
        if len(playername) > 0:
            playername = playername[:len(playername) -1]
            time.sleep(.1)
            
    elif key[K_RETURN]:
        break
    
    elif not KI.getKeyValue(key) == 'none':
        playername = playername + str(KI.getKeyValue(key).capitalize())
        time.sleep(.1)
  
    if counter%40 < 20: 
        Pname = myFont.render(playername + "_", 1,(0,0,0))
    else:
        Pname = myFont.render(playername, 1, (0,0,0))
        
    screen.blit(Pname, (340, 210))
    #340,230
    
    pygame.display.update()
    pygame.event.pump()

fr = open('savedata.txt', 'r')
filetextA = fr.readlines()
fr.close()
fr2 = open('savedata.txt')
filetextS = fr2.read()
fr2.close()



myXloc = 0
myYloc = 0
myColor = 'none'
newPlayer = True

for i in range(len(filetextA)):
    if filetextA[i][7:] == (playername + '\n'):
        newPlayer = False
        myColor = filetextA[i + 1][8:len(filetextA[i+1]) -1]
        myXloc = int(filetextA[i+2][7:len(filetextA[i+2]) -1])
        myYloc = int(filetextA[i+3][7:len(filetextA[i+3]) -1])


if newPlayer:
    while True:
        screen.blit(cselect, (0,0))
        screen.blit(red1, (120, 150))
        screen.blit(blue1, (270, 150))
        screen.blit(green1, (420, 150))
        
        clickp = pygame.mouse.get_pressed()[0]
        xpos = pygame.mouse.get_pos()[0]
        ypos = pygame.mouse.get_pos()[1]
        
        if clickp == 1:
            if (xpos >= 120 and xpos <= 180) and (ypos >= 150 and ypos <= 210):
                print "You picked red!"
                myColor = 'red'
                break
            if (xpos >= 270 and xpos <= 330) and (ypos >= 150 and ypos <= 210):
                print "You picked blue!"
                myColor = 'blue'
                break
            if (xpos >= 420 and xpos <= 480) and (ypos >= 150 and ypos <= 210):
                print "You picked green!"
                myColor = 'green'
                break
            
        
        pygame.display.update()
        pygame.event.pump()
    
#do some file reading

if newPlayer:
    myXloc = 290
    myYloc = 215
    
    TBA = '\nname = ' + playername + '\ncolor = ' + myColor + '\nxloc = ' 
    TBA = TBA + str(myXloc) + '\nyloc = ' + str(myYloc)
    
    filetextS = filetextS + TBA
    
    fw = open('savedata.txt', 'w')
    fw.write(filetextS)
    fw.close()
    
    
while True:
    
    screen.blit(background, (0,0))
    
    
    #make list of things to be blitted (based on file)
    #blit them all
    #for all things in file
    fr1 = open('savedata.txt', 'r')
    filetextA = fr1.readlines()
    fr1.close()
    
    
    for i in range(len(filetextA)):
        if filetextA[i][:4] == ('name'):
            pname = filetextA[i][7:len(filetextA[i])-1]
            color = filetextA[i + 1][8:len(filetextA[i+1]) -1]
            xloc = int(filetextA[i+2][7:len(filetextA[i+2]) -1])
            yloc = int(filetextA[i+3][7:len(filetextA[i+3]) -1])
            i = i + 3
    
            if color == 'red':
                img = red2
            elif color == 'green':
                img = green2
            elif color == 'blue':
                img = blue2
            
            name = myFont2.render(pname, 1, (255, 255, 255))
            screen.blit(name, (xloc + 10 - name.get_width()/2, yloc - 10))
            screen.blit(img, (xloc, yloc))
    
    change = False
    key = pygame.key.get_pressed()
    if(key[K_UP]):
        change = True
        if myYloc < 5:
            myYloc = 0
        else:
            myYloc = myYloc - 5
    elif(key[K_DOWN]):
        change = True
        if myYloc > 424:
            myYloc = 429
        else:
            myYloc = myYloc + 5
    elif(key[K_LEFT]):
        change = True
        if myXloc < 5:
            myXloc = 0
        else:
            myXloc = myXloc - 5
    elif(key[K_RIGHT]):
        change = True
        if myXloc > 574:
            myXloc = 579
        else:
            myXloc = myXloc + 5
            
    if change:
        fr3 = open('savedata.txt', 'r')
        filetextA = fr3.readlines()
        fr3.close()
        
        for i in range(len(filetextA)):
            if filetextA[i][7:] == (playername + '\n'):
                filetextA[i+2] = 'xloc = ' + str(myXloc) + '\n'
                filetextA[i+3] = 'yloc = ' + str(myYloc) + '\n'
                break
        
        t = ''
        for i in range(len(filetextA)):
            t = t + filetextA[i]
        
        
        fw2 = open('savedata.txt', 'w')
        fw2.write(t)
        fw2.close()
    
    
    
    
        
    pygame.display.update()
    pygame.event.pump()
