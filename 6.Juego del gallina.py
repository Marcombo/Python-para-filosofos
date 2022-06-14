import pygame
 
pantalla = pygame.display.set_mode((800,300))
pygame.display.set_caption("Juego del gallina")
 
x1 = 0
y1 = 120
 
xx1 = 770
yy1 = 120
 
x1_moviendose = 5       
 
xx1_moviendose = -5
 
reloj = pygame.time.Clock()
 
gallinaceo = True
 
while gallinaceo:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y1 += -20
                gallinaceo = False
                print("Pierde el jugador de la izquierda por haberse echado a un lado")
            elif event.key == pygame.K_s:
                y1 += 20
                gallinaceo = False
                print("Pierde el jugador de la izquierda por haberse echado a un lado")
            elif event.key == pygame.K_UP:
                yy1 += -20
                gallinaceo = False
                print("Pierde el jugador de la derecha por haberse echado a un lado")
            elif event.key == pygame.DOWN:
                yy1 += 20
                gallinaceo = False
                print("Pierde el jugador de la derecha por haberse echado a un lado")
 
    x1 += x1_moviendose
    xx1 += xx1_moviendose
 
    pantalla.fill((255,0,100))
    reloj.tick(20)
 
    gallina1 = pygame.draw.rect(pantalla, (0,0,0), [x1, y1, 30, 60])
    gallina2 = pygame.draw.rect(pantalla, (255,255,255), [xx1, yy1, 30, 60])
 
    if gallina1.colliderect(gallina2):
        gallinaceo = False
        print("Al chocar, habéis perdido los dos")
 
    pygame.display.update()
 
pygame.quit()
