import pygame

pantalla = pygame.display.set_mode((800,250))
pygame.display.set_caption("El dilema del tranvía")

x1 = 0
y1 = 75
 
x1_cambia = 20
y1_cambia = 100

reloj = pygame.time.Clock()

cambia_via = True

while cambia_via:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
             cambia_via = False
             pygame.quit()
             quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                y1 += y1_cambia
       
    x1 += x1_cambia

    pantalla.fill((100, 20, 20))
    tren = pygame.draw.rect(pantalla, (250,250,250), [x1, y1, 30, 30])
    persona1 = pygame.draw.rect(pantalla, (0,0,0), [450, 75, 30, 30])
    persona2 = pygame.draw.rect(pantalla, (0,0,0), [500, 75, 30, 30])
    persona3 = pygame.draw.rect(pantalla, (0,0,0), [550, 75, 30, 30])
    persona4 = pygame.draw.rect(pantalla, (0,0,0), [600, 75, 30, 30])
    persona5 = pygame.draw.rect(pantalla, (0,0,0), [650, 75, 30, 30])
    persona6 = pygame.draw.rect(pantalla, (0,0,0), [650, 175, 30, 30])

    if tren.colliderect(persona5):
            print("Has matado a cinco personas en lugar de a una")
            pygame.quit()
            quit()
    if tren.colliderect(persona6):
        cambia_via = False
        print("Has elegido el mal menor")
        pygame.quit()
        quit()
        
    reloj.tick(10)
    pygame.display.update()
