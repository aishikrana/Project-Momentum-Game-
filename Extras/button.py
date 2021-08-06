#button file
import pygame


#button class
class Button():
    def __init__(self, x, y, image, scale_x, scale_y):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.smoothscale(image,(scale_x, scale_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        # print(scale)

    def draw(self, window):
        action = False         #if got true then take action in main loop 
        #get mouse position
        mouse_position = pygame.mouse.get_pos()
        
        #check if mouse click this button
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:    # 0 for leftclick , 1 for middle , 2 for right click. If clicked all they return 1, if not they return 0
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on window
        window.blit(self.image, (self.rect.x, self.rect.y))
        return action