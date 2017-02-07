import pygame
import time
import random

pygame.init()

# Object class, PARTIALLY FUNCTIONING
class thingClass:
    def __init__(self, object):
        self.display_width = 800
        self.display_height = 600
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        self.thing_width = 100
        self.thing_height = 100
        self.thing_starty = -600
        self.thing_speed = 7
        self.car_width = 50
        self.rand_color = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
        def thingStart(self):
            self.thing_starty += self.thing_speed
            self.thing_startx = random.randrange(0, self.display_width - self.thing_width)
        def things(self, thingx, thingy, thingw, thingh, color):
            pygame.draw.rect(self.gameDisplay, color, [thingx, thingy, thingw, thingh])

theObject = thingClass(object)

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("jazz.wav")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
bright_red = (200,0,0)
bright_green = (0,255,0)
green = (0,180,0)

#gameDisplay = pygame.display.set_mode((theObject.display_width, display_height))
pygame.display.set_caption('Sprinkles')
clock = pygame.time.Clock()

# carImg is the little person
carImg = pygame.image.load('car.png')
#roadImg is the background (now the sky)
roadImg = pygame.image.load('road.png')

pygame.display.set_icon(carImg)

pause = False

#functioning
def quitgame():
    pygame.quit()
    quit()

# Score count, functioning    
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    theObject.gameDisplay.blit(text, (0, 0))

# Aka the little person, functioning        
def car(x, y):
    theObject.gameDisplay.blit(carImg,(x, y))

# Messages, functioning
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Messages, functioning
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((theObject.display_width/2), (display_height/2))
    theObject.gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(3)
    
    game_loop()

# Crash the game, functioning
def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
        
    largeText = pygame.font.SysFont("comicsansms",70)
    TextSurf, TextRect = text_objects("You ate a sprinkle!", largeText)
    TextRect.center = ((theObject.display_width/2),(display_height/2))
    theObject.gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

# Crash when offscreen, functioning
def offscreen():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    largeText = pygame.font.SysFont("comicsansms",70)
    TextSurf, TextRect = text_objects("Don't run offscreen!", largeText)
    TextRect.center = ((theObject.display_width/2),(theObject.display_height/2))
    theObject.gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

# Buttons click, functioning
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+50 > mouse[1] > 450:
        pygame.draw.rect(theObject.gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
          pygame.draw.rect(theObject.gameDisplay, ic, (x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2),(y+(h/2))))
    theObject.gameDisplay.blit(textSurf, textRect)

# Unpause, functioning    
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

# Paused screen, functioning
def paused():
    pygame.mixer.music.pause()

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((theObject.display_width/2),(display_height/2))
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

# Introduction screen, functioning        
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                
        theObject.gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("Sprinkles are bad for you!", largeText)
        TextRect.center = ((theObject.display_width/2), (theObject.display_height/2))
        theObject.gameDisplay.blit(TextSurf, TextRect)

        button("Go!",150,450,100,50,green,bright_green, game_loop)
        button("Quit",550,450,100,50,red,bright_red, quitgame)

        pygame.display.update()
        clock.tick(30)

# Main game loop
def game_loop():
    
    global pause

# This FUCKING MUSIC
#    pygame.mixer.music.load('jazz.wav')
#    pygame.mixer.music.play(-1)

    x = (theObject.display_width * 0.45)
    y = (theObject.display_height * 0.8)

    x_change = 0

    background_startx = 0
    background_starty = 0
    background_speed = 0.5
    background_width = 8046
    background_height = 600

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
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        
# move the background screen        
        theObject.gameDisplay.blit(roadImg, [background_startx,background_starty])
        background_startx -= background_speed

# controls the movement of the blocks
#########################################################
        theObject.thingStart()
        theObject.things(theObject.thing_startx, theObject.thing_starty, theObject.thing_width, theObject.thing_height, theObject.rand_color)
    
        car(x,y)
        things_dodged(dodged)

# increase the difficulty of the game, not completed
        if theObject.thing_starty > theObject.display_height:
            theObject.thing_starty = 0 - theObject.thing_height
            theObject.thing_startx = random.randrange(0,theObject.display_width)
            dodged += 1
            theObject.thing_speed += 1
            theObject.thing_width += (dodged * 1.2)

# if offscreen, then offscreen crash 
        if x > theObject.display_width - theObject.car_width or x < 0:
            offscreen()

# if hits object, then crash 
        if y < theObject.thing_starty+theObject.thing_height:
            if x > theObject.thing_startx and x < theObject.thing_startx + theObject.thing_width or x + theObject.theObject.car_width > theObject.thing_startx and x + theObject.car_width < theObject.thing_startx + theObject.thing_width:
                crash()
        
        pygame.display.update()
        clock.tick(60)

# actually run the loops
game_intro()
game_loop()
pygame.quit()
quit()
