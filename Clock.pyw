import os
import math as m
import pygame
from datetime import datetime
import time
import pyautogui
width, height = pyautogui.size()
pygame.init()


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %((73.15*width)/100, (46.67*height)/100)
i_icon = os.getcwd() + '.\C.png'
icon = pygame.image.load(i_icon)
pygame.display.set_icon(icon)

def main():
    

    width = 500
    height = 500
    r = 200
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("clock")
    font = pygame.font.SysFont("Segoe UI", 16)
    clock = pygame.time.Clock()
    cpt = win.get_rect().center
    white = (250, 250, 250)
    black = (0, 0, 0)
    graywhite = (224, 224, 224)
    blueblack=(131, 145, 233)
    green = (50, 205, 50)
    yellow = (255, 255, 0)
    grayred = (102, 51, 0)
    red = (255, 0, 0)
    clr = white
    color = black
    color1 = green
    color2 = graywhite
    clock = pygame.time.Clock()
    cpt = win.get_rect().center


    def time1():
        time1 = time.localtime()
        na2 = ((time1.tm_sec))
        angle = na2 * 6
        angle_rad = m.radians(angle)
        pt_x = cpt[0] + 180 * m.sin(angle_rad)
        pt_y = cpt[1] - 180 * m.cos(angle_rad)            

        pygame.draw.line(win, color1, cpt, (pt_x, pt_y), 2)


    def time2():
        time2=time.localtime()
        na1=((time2.tm_min * 60)+(time2.tm_sec))
        angle1 = na1 * 0.1
        angle1_rad = m.radians(angle1)
        pt_x1 = cpt[0] + 140 * m.sin(angle1_rad)
        pt_y1 = cpt[1] - 140 * m.cos(angle1_rad)
    
        pygame.draw.line(win, red, cpt, (pt_x1, pt_y1), 4)           



    def time3():
    
        time3 = time.localtime()
        na = ((time3.tm_hour * 60 * 60) + (time3.tm_min * 60) + (time3.tm_sec))
        angle2 = na * 0.00833
        angle2_rad = m.radians(angle2)
        pt_x2 = cpt[0] + 100 * m.sin(angle2_rad)
        pt_y2 = cpt[1] - 100 * m.cos(angle2_rad)
    
        pygame.draw.line(win, blueblack, cpt, (pt_x2, pt_y2), 4)         


    def button():
        if clr == white:
            win.fill(white)
        else:    
            win.fill(black)
            

    run = True
    while run:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                clr = white
                color = black
                color1 = green
                color2 = graywhite
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clr = black
                color = white
                color1 = yellow
                color2 = grayred
                
        button()
        
        ti = datetime.now()
        displaytime = ti.strftime(" %I : %M : %S : %p ")
        displayday = ti.strftime(" %A ")
        displaydate = ti.strftime(" %d : %B : %Y ")

        pygame.draw.circle(win, color2, cpt, 210)
        drawt = font.render(displaytime, True, color)
        win.blit(drawt, win.get_rect(center = cpt))
        
        drawd = font.render(displaydate, True, color)
        win.blit(drawd, (cpt[0] + 100, cpt[1] - 230))

        drawdy = font.render(displayday, True, color)
        win.blit(drawdy, (cpt[0] + 150, cpt[1] - 250))
        
        draw1 = font.render(str(12), True, color)
        win.blit(draw1,(cpt[0] - 5, cpt[1] - 13 - r))
        
        draw2 = font.render(str(1), True, color)
        win.blit(draw2,(cpt[0] - 4 + r * m.cos(m.radians(60)), cpt[1] - 11 - r * m.sin(m.radians(60))))
        
        draw3 = font.render(str(2), True, color)
        win.blit(draw3,(cpt[0] - 3 + r * m.cos(m.radians(30)), cpt[1] - 12 - r * m.sin(m.radians(30))))
        
        draw4 = font.render(str(3), True, color)
        win.blit(draw4,(cpt[0] + r, cpt[1] - 10))
        
        draw5 = font.render(str(4), True, color)
        win.blit(draw5,(cpt[0] - 4 + r * m.cos(m.radians(30)), cpt[1] - 11 + r * m.sin(m.radians(30))))
        
        draw6 = font.render(str(5), True, color)
        win.blit(draw6,(cpt[0] - 4 + r * m.cos(m.radians(60)), cpt[1] - 11 + r * m.sin(m.radians(60))))
        
        draw7 = font.render(str(6), True, color)
        win.blit(draw7,(cpt[0] - 4, cpt[1] - 11 + r))
        
        draw8 = font.render(str(7), True, color)
        win.blit(draw8,(cpt[0] - 5 - r * m.sin(m.radians(30)), cpt[1] - 12 + r * m.cos(m.radians(30))))
        
        draw9 = font.render(str(8), True, color)
        win.blit(draw9,(cpt[0] - 5 - r * m.sin(m.radians(60)), cpt[1] - 12 + r * m.cos(m.radians(60))))
        
        draw10 = font.render(str(9), True, color)
        win.blit(draw10,(cpt[0] - 7 - r, cpt[1] - 10))
        
        draw11 = font.render(str(10), True, color)
        win.blit(draw11,(cpt[0] - 6 - r * m.sin(m.radians(60)), cpt[1] - 10 - r * m.cos(m.radians(60))))
        
        draw12 = font.render(str(11), True, color)
        win.blit(draw12,(cpt[0] - 6 - r * m.sin(m.radians(30)), cpt[1] - 10 - r * m.cos(m.radians(30))))        

        time3()
        pygame.draw.circle(win, blueblack, cpt, 8)
        time2()
        pygame.draw.circle(win, red, cpt, 6)
        time1()
        pygame.draw.circle(win, color1, cpt, 4)


        pygame.display.update()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()
