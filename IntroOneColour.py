import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("jazz.wav")

display_width = 800
display_height = 600
car_width = 50

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
bright_red = (200,0,0)
bright_green = (0,255,0)
green = (0,180,0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Sprinkles')
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')
roadImg = pygame.image.load('road.png')

pygame.display.set_icon(carImg)

pause = False

def quitgame():
    pygame.quit()
    quit()
    
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0, 0))
        
def car(x, y):
    gameDisplay.blit(carImg,(x, y))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

##class thingClass:
##    def __init__(self, object):
##        self.gameDisplay = pygame.display.set_mode((800, 600))
##        self.thing_width = 100
##        self.thing_height = 100
##        self.thing_starty = -600
##        self.thing_speed = 7
##        self.rand_color = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
##    def thingStartx(self):
##        self.thing_startx = random.randrange(0, 800 - self.thing_width)
##        return self.thing_startx
##    def thingStarty(self):
##        self.thing_starty += self.thing_speed
##        return self.thing_starty
##    def things(thingx, thingy, thingw, thingh, color):
##        pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(3)
    
    game_loop()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
        
    largeText = pygame.font.SysFont("comicsansms",70)
    TextSurf, TextRect = text_objects("You ate a sprinkle!", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def offscreen():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    largeText = pygame.font.SysFont("comicsansms",70)
    TextSurf, TextRect = text_objects("Don't run offscreen!", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def offscreen_left():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 10

def offscreen_right():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
            if event.key == pygame.K_RIGHT:
                x_change = 0

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+50 > mouse[1] > 450:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
          pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2),(y+(h/2))))
    gameDisplay.blit(textSurf, textRect)
    
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():

    pygame.mixer.music.pause()

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()      

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)  
        
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("Sprinkles are bad for you!", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Go!",150,450,100,50,green,bright_green, game_loop)
        button("Quit",550,450,100,50,red,bright_red, quitgame)

        pygame.display.update()
        clock.tick(30)

def game_loop():
    
    global pause

    pygame.mixer.music.load('jazz.wav')
    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    background_startx = 0
    background_starty = 0
    background_speed = 0.5
    background_width = 8046
    background_height = 600

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    dodged = 0

    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

        x += x_change
        
# move the background screen        
        gameDisplay.blit(roadImg, [background_startx,background_starty])
        background_startx -= background_speed

        things(thing_startx, thing_starty, thing_width, thing_height, bright_red)

# controls the movement of the blocks
#########################################################
#        thing = thingClass(object)
#        thing.thingStartx()
#        thing.thingStarty()
#        thing.thingRect(gameDisplay, thing.rand_color, thing.thing_startx, thing.thing_starty, thing.thing_width, thing.thing_height)
#        pygame.display.update()
#########################################################
        
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
 
        if x > display_width - car_width or x < 0:
            offscreen()
 
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
 
        if y < thing_starty+thing_height:

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
