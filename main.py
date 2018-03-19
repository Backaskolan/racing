import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
<<<<<<< HEAD:racer.py
    
def game_loop():
=======



def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))    

class Car:
    def __init__(self):
        self.img = carImg = pygame.image.load('racecar.png')
        self.x, self.y = ((display_width * 0.45), (display_height * 0.8))
        self.width = 73
        self.speed = 5

    def draw(self):
        gameDisplay.blit(self.img, (self.x, self.y))

    def move(self, dir):
        self.x += dir

    def __repr__(self):
        return 'Car object at {} running at speed {}'.format((self.x, self.y), self.speed)

class Thing:
    def __init__(self):            
        self.x, self.y = (random.randrange(0, display_width),-600)
        self.speed = 4
        self.width = 100
        self.height = 100
        self.color = pygame.color.Color('pink')

    def draw(self):
        pygame.draw.rect(gameDisplay, self.color, [self.x, self.y, self.width, self.height])

    def move(self):
        self.y += self.speed


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

def crash():
    message_display('You Crashed')
    car.__init__()
    thing.__init__()
    time.sleep(2)
    print(car)
    game_loop()
    
car = Car()
thing = Thing()

def game_loop():
    x_change = 0

    thingCount = 1

    dodged = 0

>>>>>>> classes:main.py
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

<<<<<<< HEAD:racer.py
        gameDisplay.fill(pygame.color.Color('azure4'))
=======
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -(car.speed)
                if event.key == pygame.K_RIGHT:
                    x_change = car.speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        gameDisplay.fill(pygame.color.Color('azure4'))
              
        car.draw()
        thing.draw()
        car.move(x_change)
        thing.move()
        things_dodged(dodged)

        if car.x > display_width - car.width or car.x < 0:
            crash()

        if thing.y > display_height:
            thing.y = 0 - thing.height
            thing.x = random.randrange(0,display_width)
            dodged += 1
            thing.speed += 1
            car.speed += 1
            thing.width += (dodged * 1.2)

        if car.y < thing.y+thing.height:
            # print('y crossover')

            if car.x > thing.x and car.x < thing.x + thing.width or car.x+car.width > thing.x and car.x + car.width < thing.x+thing.width:
                # print('x crossover')
                crash()
        
>>>>>>> classes:main.py
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
