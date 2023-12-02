import pygame


pygame.init()

screen_width = 1080
screen_hight = 720

screen = pygame.display.set_mode((screen_width, screen_hight))

font = pygame.font.SysFont("Goudy Stout обычный", 50)
font2 = pygame.font.SysFont("TimesNewRoman", 30)
img = pygame.image.load("img/menu.jpg")
img1 = pygame.transform.scale(img, (1080, 720))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.blit(img1, (0, 0))
    text = font2.render("Start", True, (0,0,225))
    screen.blit(text, (500, 320))
    text = font.render("Welcome", True, (0, 255, 0))
    screen.blit(text, (455, 200))
    text = font2.render("Options", True, (0,0,255))
    screen.blit(text, (480, 350))
    text = font2.render("Exit", True, (255, 0, 0))
    screen.blit(text, (505, 380))

    pygame.display.update()
