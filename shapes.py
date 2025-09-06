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
    def __init__(self,color,radius,c,thickness):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.c = c
        self.thickness = thickness

    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.c,self.radius,self.thickness)

    def grow(self):
        self.radius += 10
        pygame.draw.circle(self.screen,self.color,self.c,self.radius,self.thickness)

circle3 = Circle("teal", 50,(500,190), 70)
circle1 = Circle("red", 100 ,(500,190), 0)   

screen.fill("PaleGreen")


while playing :
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            circle2 = Circle("white", 10,pygame.mouse.get_pos(),0)
            circle2.draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle3.grow()
            circle1.grow()
            pygame.display.update()
        if event.type == pygame.QUIT:
            playing=False
            pygame.quit()

    circle1.draw()
    circle3.draw()
        
    

    
