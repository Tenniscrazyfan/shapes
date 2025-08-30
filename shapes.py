import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
playing = True

class Rectangle():
    def __init__(self,color,dimension):
        self.screen = screen
        self.color = color
        self.dimension = dimension

    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.dimension)

rect1 = Rectangle("Black", (100,100,80,70))      


class Circle():
    def __init__(self,color,radius,c):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.c = c

    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.c,self.radius,0)

    def grow(self):
        self.radius += 10
        pygame.draw.circle(self.screen,self.color,self.c,self.radius,0)

circle1 = Circle("Black", 90 ,(100,190))    


while playing :
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle1.grow()
            pygame.display.update()
        if event.type == pygame.QUIT:
            playing=False
            pygame.quit()
        
    screen.fill("PaleGreen")
    rect1.draw()
    circle1.draw()
    pygame.display.update()
