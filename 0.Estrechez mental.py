import pygame, time
 
print()
print("Resetea tus ideas o morirás aplastado por tu estrechez mental.\nSolo una tecla te permitirá empezar desde cero...")
time.sleep(3)
 
ancho = 1000 
 
while ancho > 0:
    ancho -= 100
    if ancho == 0:
        print()
        print("Muerto por no pensar")
    pantalla = pygame.display.set_mode((ancho,500))
    pantalla.fill((50, 150, 50))
    pygame.display.update()
    time.sleep(1)
 
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_0:
                print("¡Has salido de la caverna!")
                escapar = False
                pygame.quit()
                quit()


