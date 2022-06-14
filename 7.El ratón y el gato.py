import pygame

pantalla = pygame.display.set_mode((660,660))
pygame.display.set_caption("El ratón y el gato")
 
x1 = 0
y1 = 0
 
xx1 = 630
yy1 = 630
 
x1_moviendose = 0       
y1_moviendose = 0

xx1_moviendose = 0
yy1_moviendose = 0

 
reloj = pygame.time.Clock()

persigue = True

while persigue:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                x1_moviendose = 0
                y1_moviendose = -10
            elif event.key == pygame.K_s:
                x1_moviendose = 0
                y1_moviendose = 10
            elif event.key == pygame.K_a:
                x1_moviendose = -10
                y1_moviendose = 0
            elif event.key == pygame.K_d:
                x1_moviendose = 10
                y1_moviendose = 0
            elif event.key == pygame.K_UP:
                xx1_moviendose = 0
                yy1_moviendose = -10
            elif event.key == pygame.K_DOWN:
                xx1_moviendose = 0
                yy1_moviendose = 10
            elif event.key == pygame.K_LEFT:
                xx1_moviendose = -10
                yy1_moviendose = 0
            elif event.key == pygame.K_RIGHT:
                xx1_moviendose = 10
                yy1_moviendose = 0
             
    x1 += x1_moviendose
    y1 += y1_moviendose
    xx1 += xx1_moviendose
    yy1 += yy1_moviendose

    pantalla.fill((155,50,50))
    reloj.tick(20)

    gato = pygame.draw.rect(pantalla, (0,0,0), [x1, y1, 60, 60])
    raton = pygame.draw.rect(pantalla, (255,255,255), [xx1, yy1, 30, 30])

    if gato.colliderect(raton):
        persigue = False
        print("El gato cazó al ratón")

    tiempo = pygame.time.get_ticks()/1000
    tiempo = int(tiempo)

    if x1 <= 0:
        x1_moviendose = 0
    elif y1 <= 0:
        y1_moviendose = 0
    elif x1 >= 600:
        x1_moviendose = 0
    elif y1 >= 600:
        y1_moviendose = 0

    if xx1 <= 0:
        xx1_moviendose = 0
    elif yy1 <= 0:
        yy1_moviendose = 0
    elif xx1 >= 630:
        xx1_moviendose = 0
    elif yy1 >= 630:
        yy1_moviendose = 0
    
    if tiempo == 10:
        persigue = False
        print("El ratón cansó al gato")
        quit()

    pygame.display.update()
