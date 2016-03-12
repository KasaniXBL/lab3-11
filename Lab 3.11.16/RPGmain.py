## RPGmain.py

import pygame,sys
from pygame.locals import*
from RPGCharacter import Character
from NEWBUTTON import Button

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1200,900))
pygame.display.set_caption('CAPTAIN COLD vs. THE FLASH')

# Set Up Button
BUTTONHEIGHT = 160
BUTTONWIDTH = 300
BGCOLOR = (0,30,50)
BCOLOR = (0,80,60)
Tcolor = (255,255,255)
DISPLAYSURF.fill(BGCOLOR)
Btext1 = ('Randomize')


BXPOS = 600 - 150
BYPOS = 900 * .65

# Instantiate Button, instantiate creates an instance - detailed information about one particular object.
#     class(height,            width,   color, textColor, label,   surf,        position)
B1 = Button(BUTTONHEIGHT, BUTTONWIDTH, BCOLOR, Tcolor, Btext1, DISPLAYSURF, (BXPOS, BYPOS))
B2 = Button(BUTTONHEIGHT, BUTTONWIDTH, BCOLOR, Tcolor, Btext1, DISPLAYSURF, (BXPOS, BYPOS))

BUTTONLIST = [B1,B2]

# find your fav character images and pass it here
Char1 = Character('Snart.png','CAPTAIN COLD',DISPLAYSURF,(100,300),200)
Char2 = Character('Flash.png','FLASH',DISPLAYSURF,(700,300),200)


def displayButtons(bList):
    for x in bList:
        x.display()    

def main():

    B1.active = True
    clickCount = 1
    B2.active = False

    while True:
        DISPLAYSURF.fill(BGCOLOR)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            ## MOUSE EVENTS
            elif event.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if B1.clicked(mouse):
                    B1.highlight = True
                    print("Hello")
                    clickCount = 2
                elif B2.clicked(mouse):
                    B2.highlight = True
                    print("Bye")
                    clickCount = 1
                    
            elif event.type == MOUSEBUTTONUP:
                if B1.clicked(mouse):
                    Char1.Randomize() ## Randomize the HP DMG
                    B1.highlight = False
                    B1.active = False
                    B2.active = True
                elif B2.clicked(mouse):
                    Char2.Randomize() ## Randomize the HP DMG
                    B2.highlight = False
                    B2.active = False
                    B1.active = True

        Char1.display()
        Char2.display() 
        displayButtons(BUTTONLIST)  
        pygame.display.update()
        


main()
