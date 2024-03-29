import pygame
import math

rect_select_img = pygame.image.load("rect_select.png")
circle_select_img = pygame.image.load("circle_select.png")
eraser_select_img = pygame.image.load("eraser.png")


rect_select_rect = rect_select_img.get_rect(center = (40,40))
circle_select_rect = circle_select_img.get_rect(center = (120,40))
eraser_select_rect = eraser_select_img.get_rect(center = (280,40))

width = 640
height = 480

'''
class Palette():
    def __init__(self, pos, spectrum_pos):
        self.image = pygame.image.load("palette.png")
        self.rect = self.image.get_rect(center = pos)
        self.spectrum_mode = False
        self.select_mode = False
        self.spectrum = pygame.image.load("color_select.jpg")
        self.spectrum_rect = self.spectrum.get_rect(center=spectrum_pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.spectrum_mode:
            screen.blit(self.spectrum, self.spectrum_rect)
            self.select_mode = True

    def select_spectrum(self, screen, mouse_pos):
        if not self.spectrum_mode and self.rect.collidepoint(mouse_pos):
            self.spectrum_mode = True

    def select_color(self, screen, mouse_pos, current_color):
        if self.spectrum_mode and self.spectrum_rect.collidepoint(mouse_pos):
            return screen.get_at(mouse_pos)
        else:
            return current_color
'''        

class Circle():
    drawn_circles = set()
    enable = False

    def __init__(self, color, screen):
        self.color = color
        self.surf = screen
        self.radius = 0
        self.center = None
        self.drawn = False


    
    def draw(self, mouse_pressed):
        if not mouse_pressed and self.center != None:
            self.drawn = True
            return
        pos = pygame.mouse.get_pos()
        if self.center == None:
            self.center = pos
      
        self.radius = math.sqrt((pos[0] - self.center[0])**2 + (pos[1] - self.center[1])**2)
        pygame.draw.circle(self.surf, self.color, self.center, self.radius)
        self.add_circle()
        

    
    def add_circle(self):
        Circle.drawn_circles.add(self)


    @classmethod
    def draw_all(cls):
        
        for inst in cls.drawn_circles:
            pygame.draw.circle(inst.surf, inst.color, inst.center, inst.radius)


class NRect():
    drawn_rects = set()
    enable = False

    def __init__(self, color, screen):
        self.color = color
        self.surf = screen
        self.start_point = None
        self.drawn = False

    def draw(self, mouse_pressed):
        if not mouse_pressed and self.start_point != None:
            self.drawn = True
            return

        pos = pygame.mouse.get_pos()
        if self.start_point == None:
            self.start_point = pos

        x = min(self.start_point[0], pos[0])
        y = min(self.start_point[1], pos[1])

        width = max(pos[0], self.start_point[0]) - x
        height = max(pos[1], self.start_point[1]) - y
        self.rect = (self.start_point[0], self.start_point[1], width, height)
        pygame.draw.rect(self.surf, self.color, self.rect)
        self.add_rect()

    def add_rect(self):
        NRect.drawn_rects.add(self)

    @classmethod
    def draw_all(cls):
        for inst in cls.drawn_rects:
            pygame.draw.rect(inst.surf, inst.color, inst.rect)


class Eraser():
    def __init__(self, bg_color, screen):
        self.enable = False
        self.surf = screen
        self.layer = pygame.Surface((width, height))
        self.color = bg_color
        self.radius = 20
        self.points = []

    def erase(self, mouse_pos):
        pygame.draw.circle(self.surf, self.color, mouse_pos, self.radius)
        self.points.append(mouse_pos)

    def draw_all(self):
        self.surf.blit(self.layer, (0,0), special_flags=pygame.BLEND_RGB_ADD)
        for x in self.points:
            pygame.draw.circle(self.surf, self.color, x, self.radius)




def main():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    clock = pygame.time.Clock()
    
    radius = 15
    points = []
    mode = "blue"
    bg_color = (0,0,0)
    

    circle = Circle((255,255,255),screen)
    nrect = NRect((255,255,255),screen)
    eraser = Eraser(bg_color, screen)

    #palette = Palette((200,40),(160,176))
    
    
    while True:

        pressed_key = pygame.key.get_pressed()

        alt = pressed_key[pygame.K_LALT] or pressed_key[pygame.K_RALT]
        ctrl = pressed_key[pygame.K_LCTRL] or pressed_key[pygame.K_RCTRL]

        screen.fill(bg_color)     



        pressed = pygame.mouse.get_pressed()
        if Circle.enable:
            circle.draw(pressed[0])
            if circle.drawn:
                circle = Circle((255,255,255),screen)
        elif NRect.enable:
            nrect.draw(pressed[0])
            if nrect.drawn:
                nrect = NRect((255,255,255),screen)
        
        
        Circle.draw_all()
        NRect.draw_all()                 
        eraser.draw_all()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl:
                    return
                if event.key == pygame.K_F4 and alt:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                if event.key == pygame.K_r:
                    mode = "red"
                elif event.key == pygame.K_g:
                    mode = "green"
                elif event.key == pygame.K_b:
                    mode = "blue"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if circle_select_button.collidepoint(event.pos):
                    Circle.enable = not Circle.enable
                    NRect.enable = eraser.enable = False
                elif rect_select_button.collidepoint(event.pos):
                    NRect.enable = not NRect.enable
                    Circle.enable = eraser.enable = False
                elif eraser_select_button.collidepoint(event.pos):
                    eraser.enable = not eraser.enable
                    Circle.enable = NRect.enable = False
                #if event.button == 1:
                #    radius = min(200, radius + 1)
                #elif event.button == 3:
                #    radius = max(1, radius - 1)
            elif event.type == pygame.MOUSEMOTION and event.buttons[0] and eraser.enable:
                eraser.erase(event.pos)

                #palette.select_spectrum(screen, mouse_pos)
                #mode = palette.select_color(screen, mouse_pos, mode)

            #    position = event.pos
            #    points = points + [position]
            #    points = points[-256:]
       


        
            
            #drawing
        '''
        i = 0
        while i < len(points) - 1:
            drawLine(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        '''
            
        pygame.draw.rect(screen, (112,128,144), (0,0,320,80))
        rect_select_button = screen.blit(rect_select_img, rect_select_rect)
        circle_select_button = screen.blit(circle_select_img, circle_select_rect)
            #palette_select_button = screen.blit(palette_select_img, palette_select_rect)
            #palette.draw(screen)
        eraser_select_button = screen.blit(eraser_select_img, eraser_select_rect)

                


        pygame.display.flip()
        clock.tick(144)
            
def drawLine(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == "blue":
        color = (c1, c1, c2)
    #elif color_mode == "red":
     #   color = (c2, c1, c1)
    #elif color_mode == "green":
     #   color = (c1, c2, c1)
    else:
        color = color_mode

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):            
        progress = 1.0 * i /iterations
        aprogress = 1 - progress

        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x,y), width)

main()



