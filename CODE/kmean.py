import pygame   #dùng thư viện pygame
pygame.init()   #khởi tạo thư viện
screen=pygame.display.set_mode((1200,700)) #tạo màn hình
pygame.display.set_caption('KMean Visualition') #ghitiêuđề
running=True
BACKGROUND=(214,214,214)
BLACK=(0,0,0)
WHITE=(255,255,255)
BACKGROUND_PANEL=(249,255,230)
font=pygame.font.SysFont('sans',40)
text_plus=font.render('+', True, WHITE)
text_min=font.render('+', True, WHITE)
while running:
    screen.fill(BACKGROUND)
    #ve giao dien -Draw interface
    #ve panel
    pygame.draw.rect(screen, BLACK, (50,50,700,500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55,55,690,490))
    #ve nut K +
    pygame.draw.rect(screen, BLACK, (850,50,50,50))
    screen.blit(text_plus, (860,50))
    #ve nut K -
    pygame.draw.rect(screen, BLACK, (950,50,50,50))
    screen.blit(text_min, (960,50))
    #ket thuc giao dien
    mouse_x, mouse_y=pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            #change K button + 
            if 850<mouse_x< 900 and 50<mouse_y<100:
                print('Press K+')
            if 950<mouse_x< 1000 and 50<mouse_y<100:
                print('Press -')
    pygame.display.flip() #cập nhật thay đổi màn hình
pygame.quit()
