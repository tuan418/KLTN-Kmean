import pygame   
pygame.init()   
screen=pygame.display.set_mode((1200,700)) 
pygame.display.set_caption('KMean Visualition') 
running=True
BACKGROUND=(214,214,214)
while running:
    screen.fill(BACKGROUND)  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.flip() 
pygame.quit()


                           
                        
                           
