import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sistema de Partículas con Movimiento Propio y Rebote")

# Colores
WHITE = (0, 0, 0)

# Clase para representar una partícula
class Particle:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = random.randint(2, 5)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.velocity.scale_to_length(random.uniform(1, 3))

    def move(self):
        self.pos += self.velocity

        # Rebote en los bordes
        if self.pos.x <= 0 or self.pos.x >= WIDTH:
            self.velocity.x *= -1
        if self.pos.y <= 0 or self.pos.y >= HEIGHT:
            self.velocity.y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.size)

# Inicializar lista de partículas
particles = [Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(100)]

# Bucle principal
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for particle in particles:
        particle.move()
        particle.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
