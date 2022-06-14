import pygame, random
 
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("borrador.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
 
class Objetos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("tiza.png")
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
 
pantalla = pygame.display.set_mode([900,600])
pygame.display.set_caption("Tabula rasa")
reloj = pygame.time.Clock()
 
puntuacion = 0
 
lista_objetos = pygame.sprite.Group()
lista_todos_sprites = pygame.sprite.Group()
 
jugador = Jugador()
lista_todos_sprites.add(jugador)
 
for cosa in range(50):
    objetos = Objetos()
    objetos.rect.x = random.randrange(870)
    objetos.rect.y = random.randrange(570)
 
    lista_objetos.add(objetos)
    lista_todos_sprites.add(objetos)
 
pizarra = True
 
while pizarra:
 
    raton = pygame.mouse.get_pos()
    jugador.rect.x = raton[0]
    jugador.rect.y = raton[1]
 
    colision = pygame.sprite.spritecollide(jugador, lista_objetos, True)
 
    for objeto in colision:
        puntuacion += 1
        print(puntuacion)
    if puntuacion == 50:
        print("Tu mente está preparada para reaprenderlo todo")
        pygame.quit()
        quit()
 
    pantalla.fill((96,128,96))
 
    lista_todos_sprites.draw(pantalla)
 
    pygame.display.flip()
    reloj.tick(60)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pizarra = False
            pygame.quit()
