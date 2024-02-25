import pygame


def draw(screen:pygame.display,rect:pygame.Rect,text,b_color,t_color):
    pygame.font.init()
    font_obj = pygame.font.Font(None, 30)
    shadow_rect = rect.copy()
    shadow_rect.x += 2
    shadow_rect.y += 2

    pygame.draw.rect(screen, t_color, shadow_rect, border_radius=5)

    text_surface = font_obj.render(text,True,t_color)
    pygame.draw.rect(screen,b_color,rect,border_radius=5)
    screen.blit(text_surface,text_surface.get_rect(center=rect.center))

class Button:
    def draw_dark(screen:pygame.display,rect:pygame.Rect,text,hover,width,height):
        if hover:
            button_color = (237,194,46)
            text_color = (119,110,101)
        else:
            button_color = (0,0,0)
            text_color = (249,246,242)

        rect.center = (width, height)
        draw(screen,rect,text,button_color,text_color)

    def draw_light(screen:pygame.display,rect:pygame.Rect,text,hover,width,height):
        if hover:
            button_color = (246,94,59)
            text_color = (249,246,242)
        else:
            button_color = (237,194,46)
            text_color = (119,110,101)

        rect.center = (width, height)
        draw(screen,rect,text,button_color,text_color)

    def draw_red(screen:pygame.display,rect:pygame.Rect,text,hover,width,height):
        if hover:
            button_color = (237,194,46)
            text_color = (119,110,101)
        else:
            button_color = (246,94,59)
            text_color = (249,246,242)

        rect.center = (width, height)
        draw(screen,rect,text,button_color,text_color)