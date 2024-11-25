import pygame   #dùng thư viện pygame
pygame.init()   #khởi tạo thư viện
screen=pygame.display.set_mode((1200,700)) #tạo màn hình
pygame.display.set_caption('KMean Visualition') #ghitiêuđề
running=True
BACKGROUND=(214,214,214)
while running:
    screen.fill(BACKGROUND)  #làm đầy màn hình với màu nền
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.flip() #cập nhật thay đổi màn hình
pygame.quit()