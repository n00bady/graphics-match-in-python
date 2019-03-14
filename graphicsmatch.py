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
    # "Spin" randomly one time the slots
    def Spin(self):
        self.luck = (random.randint(0, 5), random.randint(0, 5), random.randint(0, 5))
    # Calculate the points
    def GetScore(self):
        if self.luck[0] == self.luck[1] == self.luck[2]:
            points = 75
        elif self.luck[0] == self.luck[1]:
            if self.luck[0] in [0, 1, 2]:
                points = 40
            else:
                points = 10
        elif self.luck[0] == self.luck[2]:
            points = 10
        else:
            points = -10
        return points

# Cheer for getting a jackpot  7 7 7
def jackpot(surface, font, surfacecolor):
    x0 = random.randint(100, 1000)
    y0 = random.randint(50, 550)
    x1 = random.randint(100, 1000)
    y1 = random.randint(50, 550)
    x2 = random.randint(100, 1000)
    y2 = random.randint(50, 550)
    wintext0 = font.render("J A C K P O T ! ! !", True, (210, 0, 0))
    wintext1 = font.render("J A C K P O T ! ! !", True, (0, 210, 0))
    wintext2 = font.render("J A C K P O T ! ! !", True, (0, 0, 250))
    surface.blit(wintext0, (x0, y0))
    surface.blit(wintext1, (x1, y1))
    surface.blit(wintext2, (x2, y2))
    

# -- Main Fun --

surface_color_fade = [10, 80, 200, 2] # lowering the last number means the face out/in is slower

def main():
    # Pygame ininialization
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Graphics Match v0.1")
    
    # The slot machine images
    slot_images = ('lemon.png', 'bar.png', 'cherry.png', 'bell.png', 'blueberry.png', 'seven.png')
    slotmachine = Spinner(slot_images)
    
    # Initial values
    quitprogram = False
    spacepressed = False
    cheat = False
    score = 0
    framerate = 60 
    spacepressed = True
    # Coordinates for the score and the images
    # If you change the images make sure they are 128x128 or they will not center properly
    x = 509
    y = 232   
    scoreX = 1000
    scoreY = 650
    pointsX = 920
    pointsY = 310
    gg = pygame.mixer.Sound('gg.ogg')

    # Window resolution and background color
    windowsize = (1280, 720)
    surfacecolor = (10, 80, 200)
    screen = pygame.display.set_mode(windowsize, DOUBLEBUF)
    screen.fill(surfacecolor)
    

    # Clock
    clock = pygame.time.Clock()

    # Fonts for the text 
    #Maybe I should change this to Arial or something more stantard 
    textfont = pygame.font.SysFont("Arial", 22)
    textfont2 = pygame.font.SysFont("Arial", 42, True)
   
    # Create a new surface to help me fade out the points text in the main loop
    newSurf = pygame.Surface((200, 40)).convert_alpha()
    newSurf.fill(surface_color_fade)

    # -- Main loop --
    while not quitprogram:
        # - Old way to calculate fps -
        #time = clock.tick(framerate)
        # Shows the current fps on the upperleft corner
        #fpstext = textfont.render(str(round((1000/time), 1)), True, (255, 0, 0), (255, 255, 0)) # For some reason it run in 62.5fps
        # - New way to calculate fps - 
        #clock.tick(framerate)
        clock.tick_busy_loop(framerate)
        fpstext = textfont.render(str(int(clock.get_fps())), True, (255, 0, 0), (255, 255, 0)) # For some reason it run in 62.5fps
        pygame.draw.rect(screen, (255, 255, 0), (0, 0, 40, 30))
        screen.blit(fpstext, (0, 0))
        # There is something weird happening with the fps, don't know excaclty what... 🤔
        
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

        # What happens when you push the buttons
        if spacepressed == True:
            screen.fill(surfacecolor)
            for draws in range(0, 150):              
                slotmachine.Spin()
                x1 = x
                pygame.draw.rect(screen, (0, 0, 0), (x1, y, 393, 128))
                for i in slotmachine.luck:
                    screen.blit(slotmachine.slot[i], (x1, y))
                    x1 = x1 + slotmachine.slot[i].get_width() + 3
                pygame.display.update()
            # Show how many points you got in the last spin
            points = slotmachine.GetScore()
            if points < 0:
                pointstext = textfont.render("You lose: "+str(points), True, (230, 220, 55))
                pygame.draw.rect(screen, (10, 80, 200), (pointsX, pointsY, 200, 40))
                screen.blit(pointstext, (pointsX, pointsY))
            elif points == 75:
                # Something different happens when you get a jackpot!
                jackpot(screen, textfont2, surfacecolor)
                gg.play()
            else:
                pointstext = textfont.render("You win: "+str(points), True, (230, 220, 55))
                pygame.draw.rect(screen, (10, 80, 200), (pointsX, pointsY, 200, 40))
                screen.blit(pointstext, (pointsX, pointsY))
                gg.play()
            # Calculate Score
            score = score + slotmachine.GetScore()
            # Show score
            scoretext = textfont.render("Score: "+str(score), True, (255, 255, 255))
            pygame.draw.rect(screen, (255, 0, 0), (scoreX, scoreY, 400, 30))
            screen.blit(scoretext, (scoreX, scoreY))
            spacepressed = False
        if cheat == True:
            if score < 0:
                score = -score
                scoretext = textfont.render("Score: "+str(score), True, (255, 255, 255))
                pygame.draw.rect(screen, (255, 0, 0), (scoreX, scoreY, 400, 30))
                screen.blit(scoretext, (scoreX, scoreY))
            cheat = False
        # Fadeing out the points text by putting a new surface on top of it and fading it in slowly
        screen.blit(newSurf, (pointsX, pointsY))

        pygame.display.flip() 
    pygame.mixer.quit()
    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
