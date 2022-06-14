import pygame, random

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("borrador.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 300
    def movimiento(self, direccionx, direcciony):
        self.rect.x += direccionx
        self.rect.y += direcciony
        
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, ruta_imagen, posX, posY, deltaX, deltaY):
        super().__init__()
        self.image = pygame.image.load(ruta_imagen)
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()

        self.rect.x = posX
        self.rect.y = posY

        self.deltaX = deltaX
        self.deltaY = deltaY
        
    def update(self):
        self.rect.x += self.deltaX
        self.rect.y += self.deltaY
        
        if self.rect.y > 2000:
            if puntuacion == 100:
                print("¡Perfecto! Has evitado todas las amenazas")
                pygame.quit()
                quit()
            else:
                print("¡Vaya! No has podido evitar", int(100-puntuacion), "amenazas")
                pygame.quit()
                quit()

pantalla = pygame.display.set_mode([900,600])
pygame.display.set_caption("El peor de los mundos posibles")
reloj = pygame.time.Clock()

puntuacion = 100

lista_riesgos = pygame.sprite.Group()
lista_todos_sprites = pygame.sprite.Group()

jugador = Jugador()
lista_todos_sprites.add(jugador)

for amenaza in range(25):
    lista_riesgos.add((Enemigo("tiza.png", random.randrange(0, 900), random.randrange(-1000, 0), 0, 1)),
                      (Enemigo("jirafa.png", random.randrange(0, 900), random.randrange(600, 1600), 0, -1)),
                      (Enemigo("heroe.png", random.randrange(-1000, 0), random.randrange(0, 600), 1, 0)),
                      (Enemigo("gatete.png", random.randrange(900, 1900), random.randrange(0, 600), -1, 0)))
    lista_todos_sprites.add(lista_riesgos)
    
mundo = True

while mundo:
    tecla = pygame.key.get_pressed()

    if tecla[pygame.K_RIGHT]:
        jugador.movimiento(2,0)
    elif tecla[pygame.K_LEFT]:
        jugador.movimiento(-2,0)
    elif tecla[pygame.K_UP]:
        jugador.movimiento(0,-2)
    elif tecla[pygame.K_DOWN]:
        jugador.movimiento(0,2)
    
    colision = pygame.sprite.spritecollide(jugador, lista_riesgos, True)

    for peligro in colision:
        puntuacion -= 1
        
    pantalla.fill((96,128,96))

    lista_todos_sprites.draw(pantalla)
    lista_todos_sprites.update()

    pygame.display.update()
    reloj.tick(200)
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mundo = False
            pygame.quit()
