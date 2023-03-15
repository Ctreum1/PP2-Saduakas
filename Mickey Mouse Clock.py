import pygame

pygame.init()
size = [600, 600]
screen = pygame.display.set_mode(size)
FPS = 60
clock = pygame.time.Clock()
pygame.display.set_caption('Mickey Mouse Clock')
mickey_img = pygame.image.load('mickey.png')
done = True

digits = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    11: 'XI',
    12: 'XII'

}
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False


    screen.fill((255, 255, 255))
    mickey = screen.blit(mickey_img, (0.1, 0.1))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()