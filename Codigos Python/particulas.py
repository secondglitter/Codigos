import pygame
import random
import math

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Efecto Visual")

# Colores
WHITE = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clase para representar una partícula
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice([RED, GREEN, BLUE])
        self.size = random.randint(2, 5)
        self.speed = random.uniform(0.1, 2)
        self.direction = random.uniform(0, 2 * math.pi)

    def move(self):
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# Función para crear una explosión de partículas
def create_explosion(x, y):
    particles = []
    for _ in range(100):
        particle = Particle(x, y)
        particles.append(particle)
    return particles

# Inicializar lista de partículas
particles = []

# Bucle principal
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        particles.extend(create_explosion(mouse_pos[0], mouse_pos[1]))

    for particle in particles:
        particle.move()
        particle.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
