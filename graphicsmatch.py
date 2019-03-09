# =======================================================================================================
#
# Graphics Match is an attempt from me to learn python and pygame for the fun of it.
# Author: n00bady
# 
# =======================================================================================================

import pygame
import random # Not truelly random ¯\_(ツ)_/¯
from pygame.locals import * # I don't know what I need, so import everything :)
from sys import exit

class Spinner:
    def __init__(self, images):
        self.slot = []
        for image in images:
            self.slot.append(pygame.image.load(image))
    # Spin the slots (note: Should rewrite in a way so that it doesn't need to call pygame.display.update() and all the screen 
    # updates happen in the main)
    def Spin(self):
        self.luck = (random.randint(0, 5), random.randint(0, 5), random.randint(0, 5))
#         x1 = x
#         for i in self.luck:
#             surface.blit(self.slot[i], (x1, y))
#             x1 = x1 + self.slot[i].get_width() + 3
        return self.luck
    # Calculate the Score Not the actuall calculation yes just something to see if it works
    def GetScore(self):
        if self.luck[0] == self.luck[1] == self.luck[2]:
            points = 100
        return points

# -- Main Fun --

def main():
    pygame.init()
    pygame.display.set_caption("Graphics Match v0.1")
    
    slot_images = ('lemon.png', 'bar.png', 'cherry.png', 'bell.png', 'blueberry.png', 'seven.png')
    slotmachine = Spinner(slot_images)
    
    quitprogram = False
    spacepressed = False
    cheat = False

    windowsize = (1280, 720)
    surfacecolor = (10, 80, 200)
    screen = pygame.display.set_mode(windowsize, DOUBLEBUF)
    clock = pygame.time.Clock()
    framerate = 60
    textfont = pygame.font.SysFont("Cantarell", 22)
    screen.fill(surfacecolor)
    
    # -- main loop --
    while not quitprogram:
       # Pretty sure a static background don't need to run inside the main loop 
       # screen.fill(surfacecolor)
        time = clock.tick(framerate)
        # Shows the current fps on the upperleft corner
        fpstext = textfont.render(str(round((1000/time), 1)), True, (255, 0, 0), (255, 255, 0)) # For some reason it run in 62.5fps
        screen.blit(fpstext, (0, 0))  

        # Event handler ?
        for event in pygame.event.get():
            if event.type == QUIT:
                quitprogram = True
            if event.type == KEYDOWN:
                keyboardinput = event.key
                if keyboardinput == K_q:
                    quitprogram = True
                if keyboardinput == K_SPACE:
                    spacepressed = True
                if keyboardinput == K_c:
                    cheat = True

        if spacepressed == True:
            spacepressed == False
            x = 509
            y = 232
            for draws in range(0, 10):              
                result = slotmachine.Spin()
                x1 = x
                for i in result:
                    screen.blit(slotmachine.slot[i], (x1, y))
                    x1 = x1 + slotmachine.slot[i].get_width() + 3

        pygame.display.update()
        
    
    
    
    pygame.quit()
    exit()


if __name__ == "__main__":
    main()
