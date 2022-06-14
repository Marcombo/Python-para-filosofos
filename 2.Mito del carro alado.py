import pygame

pantalla = pygame.display.set_mode((600,600))
 
y1 = 300
y1_cambia = 6
 
reloj = pygame.time.Clock()
ritmo = 12

volar = True

while volar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             quit()
         

    tiempo = pygame.time.get_ticks()/1000
    tiempo = int(tiempo)
    
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_SPACE]:
        y1_cambia += -2
    if not tecla[pygame.K_SPACE]:
        y1_cambia += 1
        ritmo += 0.07
    if y1 < 0 or y1 > 600:
        volar = False
        print("¡Has perdido el equilibrio!")
        print("Has conseguido " + str(tiempo) + " puntos")
        pygame.quit()
        quit()

    y1 += y1_cambia

    pantalla.fill((50, 10, 255))
    pygame.draw.rect(pantalla, (0, 0, 0), [300, y1, 30, 30])
    pygame.display.update()
    reloj.tick(ritmo)
