import pygame
import os
import mapProperties
####

class PygView(object):

	
    def __init__(self, width=640, height=400, fps=30):
        """Initialize pygame, window, background, font,...
        """
        mapp = mapProperties.mapData()
        pygame.init()
        pygame.display.set_caption("SpeechToTextRPG")
        self.width = mapp.getPixelsX()
        self.height = mapp.getPixelsY()
        #self.height = width // 4
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.font = pygame.font.SysFont('mono', 10, bold=False)


    def run(self):
        """The mainloop
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            self.draw_text("Hello World", 1)
            self.draw_text("Yellow World!", 2)
            pygame.display.flip()
            testImage = pygame.image.load(os.path.join('data', 'Testimg.png'))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(testImage, (0, 0))

        pygame.quit()


    def draw_text(self, text, num):
        """Center text in window
        """
        fw, fh = self.font.size(text) # fw: font width,  fh: font height
        surface = self.font.render(text, True, (255, 255, 255))
        # // makes integer division in python3
        self.screen.blit(surface, ((self.width - fw-5), ((self.height - fh) - (fh*num))))

####

if __name__ == '__main__':

    # call with width of window and fps
    PygView(640, 400).run()
