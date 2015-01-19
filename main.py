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

xpos = 0
ypos = 0
color = 'none'

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
            color = 'red'
            break
        if (xpos >= 270 and xpos <= 330) and (ypos >= 150 and ypos <= 210):
            print "You picked blue!"
            color = 'blue'
            break
        if (xpos >= 420 and xpos <= 480) and (ypos >= 150 and ypos <= 210):
            print "You picked green!"
            color = 'green'
            break
        
    
    pygame.display.update()
    pygame.event.pump()
    
#do some file reading

xloc = 290
yloc = 215
    
while True:
    
    screen.blit(background, (0,0))
    #make list of things to be blitted (based on file)
    #blit them all
    #for all things in file
    
    if color == 'red':
        img = red2
    elif color == 'green':
        img = green2
    elif color == 'blue':
        img = blue2
        
    #obtain locations
    name = myFont2.render(playername, 1, (255, 255, 255))
    screen.blit(name, (xloc + 10 - name.get_width()/2, yloc - 10))
    screen.blit(img, (xloc, yloc))
    
    key = pygame.key.get_pressed()
    if(key[K_UP]):
        if yloc < 5:
            yloc = 0
        else:
            yloc = yloc - 5
    elif(key[K_DOWN]):
        if yloc > 424:
            yloc = 429
        else:
            yloc = yloc + 5
    elif(key[K_LEFT]):
        if xloc < 5:
            xloc = 0
        else:
            xloc = xloc - 5
    elif(key[K_RIGHT]):
        if xloc > 574:
            xloc = 579
        else:
            xloc = xloc + 5
    
        
    pygame.display.update()
    pygame.event.pump()
    

