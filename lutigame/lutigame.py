import pygame


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Times New Roman", 50)
font2 = pygame.font.SysFont("Times New Roman", 50)

main_fon = pygame.image.load("выживалово/ОГОНЬ.jpg")
main_fon = pygame.transform.scale(main_fon, (800, 700))

main_sensei = pygame.image.load("выживалово/волкобой.jpg")
main_sensei = pygame.transform.scale(main_sensei, (150, 150))

main_evil = pygame.image.load("кратос/кратос.jpg")
main_evil = pygame.transform.scale(main_evil, (150, 150))




x,y = 200, 50
x1,y1 = 290, 200
x2,y2 = 290, 300
speed = 1
x_sensei, y_sensei = 10, 80



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    screen.blit(main_fon, (0, 0))
    screen.blit(main_evil, (700, 10))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x_sensei +=speed
    elif keys[pygame.K_s]:
        y_sensei +=speed
    elif keys[pygame.K_w]:
        y_sensei -= speed
    elif keys[pygame.K_a]:
        x_sensei -=speed
    elif



    screen.blit(main_sensei, (x_sensei, y_sensei))


    pygame.display.update()
