import pygame
import asyncio

pygame.init()

IMAGE_L1 = pygame.transform.scale(pygame.image.load("data/image-1.png"), (125, 83))
IMAGE_L2 = pygame.transform.scale(pygame.image.load("data/image-2.png"), (125, 83))
IMAGE_L3 = pygame.transform.scale(pygame.image.load("data/image-3.png"), (125, 83))
LOGO = pygame.transform.scale(pygame.image.load("data/image-4.png"), (150, 80))

class Game():
    def __init__(self):
        self.running = True
        self.game_active = True
        self.menu_active = False
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((900, 400))

    def game_loop(self):
        self.screen.fill((0, 0, 0))

        box.update()
        box.draw()
        vis.draw()

        pygame.display.update()
        self.clock.tick(60)

    def menu_loop(self):
        pygame.display.update()
        self.clock.tick(60)

class ClickBox():
    def __init__(self):
        self.image = IMAGE_L1
        self.image_rect = self.image.get_rect(center=(450, 200))

        self.level_state = None

        self.counter = 0

    def level_1(self):
        self.image = IMAGE_L2
        self.image_rect = self.image.get_rect(center=self.image_rect.center)

    def level_2(self):
        self.image = IMAGE_L3
        self.image_rect = self.image.get_rect(center=self.image_rect.center)

    def update(self):
        if self.counter >= 100:
            self.level_state = "level_one"
            box.level_1()

        if self.counter >= 500:
            self.level_state = "level_two"
            box.level_2()

    def draw(self):
        game.screen.blit(self.image, self.image_rect)

class Visuals:
    def __init__(self):
        self.large_font = pygame.font.SysFont("Arial", 32, False)
        self.small_font = pygame.font.SysFont("Arial", 18, False)
        self.logo_image = LOGO
        self.colour = (255, 0, 0)
    
    def draw(self):
        self.score_txt = self.large_font.render(f"Clicks: {box.counter}", True, self.colour)
        game.screen.blit(self.score_txt, ((900 - self.score_txt.get_width()) // 2, 100))
        game.screen.blit(self.logo_image, ((900 - 150) // 2, 0))
game = Game()
box = ClickBox()
vis = Visuals()

async def main():
    while game.running:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if box.image_rect.collidepoint(mouse_position):
                        box.counter += 1
                        print(f"PLANE CLICKED ||| {box.counter}")

        if game.game_active:
            game.game_loop()

        elif game.menu_active:
            game.menu_loop()

        await asyncio.sleep(1)

    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())