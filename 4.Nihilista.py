import pygame

pantalla = pygame.display.set_mode((500,500))
pygame.display.set_caption("Nihilista")

x1 = 0
y1 = 0
z1 = 20
zz1 = 20

x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()

negrura = True

while negrura:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 
    x1 = x1 + x1_change
    y1 = y1 + y1_change

    pantalla.fill((200,200,250))
    nihil = pygame.draw.rect(pantalla, (0,0,0), [x1, y1, z1, zz1])
    nausea = pygame.draw.rect(pantalla, (200,200,250), [250, 250, 20, 20])
        
    if nihil.colliderect(nausea):
        z1 = z1+2
        zz1 = zz1+2
    if x1 < 0 and y1 < 0 and z1 > 500 and zz1 > 500:
        negrura = False
        print("La nada se ha adueñado de tu ser")
        pygame.quit()
        quit()

    pygame.display.update()
    clock.tick(20)
