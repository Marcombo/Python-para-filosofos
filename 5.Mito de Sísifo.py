import pygame
 
pantalla = pygame.display.set_mode((400,700))
pygame.display.set_caption("El mito de Sísifo")

heroe = pygame.image.load("heroe.png")
heroe = pygame.transform.scale(heroe, (100,200))

piedra = pygame.image.load("roca.png")
piedra = pygame.transform.scale(piedra, (100,100))

y1 = 500
yy1 = 300
 
y1_cambia = -10
yy1_cambia = -10
 
reloj = pygame.time.Clock()
 
maldicion = True
 
while maldicion:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
             maldicion = False
             pygame.quit()
             quit()
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_SPACE]:
            y1 += y1_cambia
 
    pantalla.fill((255, 100, 100))
    
    sisifo = pantalla.blit(heroe, (150,y1))
    roca = pantalla.blit(piedra, (150,yy1))

    if sisifo.colliderect(roca):
        yy1 += yy1_cambia
    if yy1 < 0:
        y1 += 400
        yy1 += 400

    reloj.tick(30)
    pygame.display.update()
