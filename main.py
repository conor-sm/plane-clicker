import pygame
import asyncio

pygame.init()

class Game():
    def __init__(self):
        self.running = True
        self.game_active = True
        self.menu_active = False
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((900, 400))

    def game_loop(self):
        self.rect = pygame.draw.rect(self.screen, (255, 0, 0),(pygame.Rect(125, 83, (900 + 125) // 2, ((400 + 83) // 2))))
        pygame.display.update()
        self.clock.tick(60)

    def menu_loop(self):
        pygame.display.update()
        self.clock.tick(60)

#class ClickBox():
 #   def __init__(self):


async def main():
    game = Game()
    #box = ClickBox()
    while game.running:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and game.rect.collidepoint(mouse_position):
                print("PLANE CLICKED")

        if game.game_active:
            game.game_loop()

        elif game.menu_active:
            game.menu_loop()

        await asyncio.sleep(1)

    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())