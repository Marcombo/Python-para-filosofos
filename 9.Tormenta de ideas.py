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
    def update(self):
        self.rect.y += 1
        if self.rect.y > 900:
            print("Has conseguido", int(puntuacion), "ideas nuevas")
            pygame.quit()
            quit()
 
pantalla = pygame.display.set_mode([900,600])
pygame.display.set_caption("Tormenta de ideas")
reloj = pygame.time.Clock()
 
puntuacion = 0
 
lista_objetos = pygame.sprite.Group()
lista_todos_sprites = pygame.sprite.Group()
 
jugador = Jugador()
lista_todos_sprites.add(jugador)
 
for cosa in range(50):
    objetos = Objetos()
    objetos.rect.x = random.randrange(0,900)
    objetos.rect.y = random.randrange(-400,0)
 
    lista_objetos.add(objetos)
    lista_todos_sprites.add(objetos)
 
tormenta = True
 
while tormenta:
 
    raton = pygame.mouse.get_pos()
    jugador.rect.x = raton[0]
    jugador.rect.y = raton[1]
 
    colision = pygame.sprite.spritecollide(jugador, lista_objetos, True)
 
    for objeto in colision:
        puntuacion += 1
 
    pantalla.fill((96,128,96))
 
    lista_todos_sprites.draw(pantalla)
    lista_todos_sprites.update()
 
    pygame.display.flip()
    reloj.tick(150)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tormenta = False
            pygame.quit()
