import pygame, time
 
print()
print("Resetea tus ideas o morirás ahogado.\nSolo una tecla te permitirá bucear...")
time.sleep(3)
 
baja = 500
agua = 50
 
while agua < 600:
  agua += 50
  baja += -50
  if agua == 600:
    print("Te has ahogado en tus propios pensamientos")
    pygame.quit()
    quit()
  pantalla = pygame.display.set_mode((700,500))
  pantalla.fill((0,0,0))
  pygame.draw.rect(pantalla, (0,0,255), [0,baja,700,agua])
  pygame.display.update()
  time.sleep(1)
 
  for evento in pygame.event.get():
    if evento.type == pygame.KEYDOWN:
      if evento.key == pygame.K_b:
        print("¡No te has ahogado!")
        escapar = False
        pygame.quit()
        quit()
 
