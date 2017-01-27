import pygame,time
pygame.init()
black = [0,0,0]
white = [255,255,255]
red = [255, 0, 0]
gray = [211,211,211]
green = [0,255,0]
blue = [0, 0, 255]
size = [300, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
screen.fill(gray)
done = False
even,odd = False,True
Flag = True
Flag1 = False
Flag2 = False
win = False
win2 = False
draw = False
end = True
reset = False
mass = ['']*9
pygame.display.set_caption("KTVR-16 Lomovskoy Kirill")
print("Знак X | 0")
print("----------")
#*******************************
def DrawLine():
    pygame.draw.line(screen,black,[100,0],[100,300],2)
    pygame.draw.line(screen,black,[200,0],[200,300],2)
    pygame.draw.line(screen,black,[0,100],[300,100],2)
    pygame.draw.line(screen,black,[0,200],[300,200],2)
def Cord(Flag,Flag1,Flag2):
    xy = (0,0)
    xy1 = xy
    if Flag2 == False:
        time.sleep(0.5)
        Flag2 = True
        return xy,Flag2
    if Flag1 == True:
        if event.type == pygame.MOUSEBUTTONDOWN and Flag == True:
            if event.button == 1:
                xy1 = event.pos
                Flag = False
            if event.type == pygame.MOUSEBUTTONUP:
                Flag = True
        if xy1 != xy:
            return xy1,Flag2
        else:
            return xy,Flag2
def XoX(xy,even,odd,mass):
    x = xy[0]
    y = xy[1]
    if odd == True and x != 0 and y != 0:
        if x > 0 and y > 0 and x < 100 and y < 100 and mass[0] == '':
            pygame.draw.line(screen,red,[10,10],[90,90],2)
            pygame.draw.line(screen,red,[10,90],[90,10],2)
            mass[0] = 'x'
            even,odd = True,False
        if x > 100 and y > 0 and x < 200 and y < 100 and mass[1] == '':
            pygame.draw.line(screen,red,[110,10],[190,90],2)
            pygame.draw.line(screen,red,[110,90],[190,10],2)
            mass[1] = 'x'
            even,odd = True,False
        if x > 200 and y > 0 and x < 300 and y < 100 and mass[2] == '':
            pygame.draw.line(screen,red,[210,10],[290,90],2)
            pygame.draw.line(screen,red,[210,90],[290,10],2)
            mass[2] = 'x'
            even,odd = True,False
        if x > 0 and y > 100 and x < 100 and y < 200 and mass[3] == '':
            pygame.draw.line(screen,red,[10,110],[90,190],2)
            pygame.draw.line(screen,red,[10,190],[90,110],2)
            mass[3] = 'x'
            even,odd = True,False
        if x > 100 and y > 100 and x < 200 and y < 200 and mass[4] == '':
            pygame.draw.line(screen,red,[110,110],[190,190],2)
            pygame.draw.line(screen,red,[110,190],[190,110],2)
            mass[4] = 'x'
            even,odd = True,False
        if x > 200 and y > 100 and x < 300 and y < 200 and mass[5] == '':
            pygame.draw.line(screen,red,[210,110],[290,190],2)
            pygame.draw.line(screen,red,[210,190],[290,110],2)
            mass[5] = 'x'
            even,odd = True,False
        if x > 0 and y > 200 and x < 100 and y < 300 and mass[6] == '':
            pygame.draw.line(screen,red,[10,210],[90,290],2)
            pygame.draw.line(screen,red,[10,290],[90,210],2)
            mass[6] = 'x'
            even,odd = True,False
        if x > 100 and y > 200 and x < 200 and y < 300 and mass[7] == '':
            pygame.draw.line(screen,red,[110,210],[190,290],2)
            pygame.draw.line(screen,red,[110,290],[190,210],2)
            mass[7] = 'x'
            even,odd = True,False
        if x > 200 and y > 200 and x < 300 and y < 300 and mass[8] == '':
            pygame.draw.line(screen,red,[210,210],[290,290],2)
            pygame.draw.line(screen,red,[210,290],[290,210],2)
            mass[8] = 'x'
            even,odd = True,False
        x,y = 0,0
    if even == True and x != 0 and y != 0:
        if x > 0 and y > 0 and x < 100 and y < 100 and mass[0] == '':
            pygame.draw.circle(screen,green,[50,50],40,2)
            mass[0] = 'y'
            even,odd = False,True
        if x > 100 and y > 0 and x < 200 and y < 100 and mass[1] == '':
            pygame.draw.circle(screen,green,[150,50],40,2)
            mass[1] = 'y'
            even,odd = False,True
        if x > 200 and y > 0 and x < 300 and y < 100 and mass[2] == '':
            pygame.draw.circle(screen,green,[250,50],40,2)
            mass[2] = 'y'
            even,odd = False,True
        if x > 0 and y > 100 and x < 100 and y < 200 and mass[3] == '':
            pygame.draw.circle(screen,green,[50,150],40,2)
            mass[3] = 'y'
            even,odd = False,True
        if x > 100 and y > 100 and x < 200 and y < 200 and mass[4] == '':
            pygame.draw.circle(screen,green,[150,150],40,2)
            mass[4] = 'y'
            even,odd = False,True
        if x > 200 and y > 100 and x < 300 and y < 200 and mass[5] == '':
            pygame.draw.circle(screen,green,[250,150],40,2)
            mass[5] = 'y'
            even,odd = False,True
        if x > 0 and y > 200 and x < 100 and y < 300 and mass[6] == '':
            pygame.draw.circle(screen,green,[50,250],40,2)
            mass[6] = 'y'
            even,odd = False,True
        if x > 100 and y > 200 and x < 200 and y < 300 and mass[7] == '':
            pygame.draw.circle(screen,green,[150,250],40,2)
            mass[7] = 'y'
            even,odd = False,True
        if x > 200 and y > 200 and x < 300 and y < 300 and mass[8] == '':
            pygame.draw.circle(screen,green,[250,250],40,2)
            mass[8] = 'y'
            even,odd = False,True
        x,y = 0,0
    return even,odd,mass
def inspection(mass,draw,win2):
    winx1,winx2,winx3,winx4,winx5,winx6,winx7,winx8, = False,False,False,False,False,False,False,False
    winy1,winy2,winy3,winy4,winy5,winy6,winy7,winy8, = False,False,False,False,False,False,False,False
    if mass[0] == 'x' and mass[1] == 'x' and mass[2] == 'x':
        win2 = False
        winx1 = True
        pygame.draw.line(screen,red,[10,50],[290,50],4)
        return winx1,draw,win2
    if mass[3] == 'x' and mass[4] == 'x' and mass[5] == 'x':
        winx2 = True
        win2 = False
        pygame.draw.line(screen,red,[10,150],[290,150],4)
        return winx2,draw,win2
    if mass[6] == 'x' and mass[7] == 'x' and mass[8] == 'x':
        winx3 = True
        win2 = False
        pygame.draw.line(screen,red,[10,250],[290,250],4)
        return winx3,draw,win2
    if mass[0] == 'x' and mass[3] == 'x' and mass[6] == 'x':
        winx4 = True
        win2 = False
        pygame.draw.line(screen,red,[50,10],[50,290],4)
        return winx4,draw,win2
    if mass[1] == 'x' and mass[4] == 'x' and mass[7] == 'x':
        winx5 = True
        win2 = False
        pygame.draw.line(screen,red,[150,10],[150,290],4)
        return winx5,draw,win2
    if mass[2] == 'x' and mass[5] == 'x' and mass[8] == 'x':
        winx6 = True
        win2 = False
        pygame.draw.line(screen,red,[250,10],[250,290],4)
        return winx6,draw,win2
    if mass[0] == 'x' and mass[4] == 'x' and mass[8] == 'x':
        winx7 = True
        win2 = False
        pygame.draw.line(screen,red,[10,10],[290,290],4)
        return winx7,draw,win2
    if mass[2] == 'x' and mass[4] == 'x' and mass[6] == 'x':
        winx8 = True
        win2 = False
        pygame.draw.line(screen,red,[290,10],[10,290],4)
        return winx8,draw,win2
    if mass[0] == 'y' and mass[1] == 'y' and mass[2] == 'y':
        winy1 = True
        win2 = True
        pygame.draw.line(screen,green,[10,50],[290,50],4)
        return winy1,draw,win2
    if mass[3] == 'y' and mass[4] == 'y' and mass[5] == 'y':
        winy2 = True
        win2 = True
        pygame.draw.line(screen,green,[10,150],[290,150],4)
        return winy2,draw,win2
    if mass[6] == 'y' and mass[7] == 'y' and mass[8] == 'y':
        winy3 = True
        win2 = True
        pygame.draw.line(screen,green,[10,250],[290,250],4)
        return winy3,draw,win2
    if mass[0] == 'y' and mass[3] == 'y' and mass[6] == 'y':
        winy4 = True
        win2 = True
        pygame.draw.line(screen,green,[50,10],[50,290],4)
        return winy4,draw,win2
    if mass[1] == 'y' and mass[4] == 'y' and mass[7] == 'y':
        winy5 = True
        win2 = True
        pygame.draw.line(screen,green,[150,10],[150,290],4)
        return winy5,draw,win2
    if mass[2] == 'y' and mass[5] == 'y' and mass[8] == 'y':
        winy6 = True
        win2 = True
        pygame.draw.line(screen,green,[250,10],[250,290],4)
        return winy6,draw,win2
    if mass[0] == 'y' and mass[4] == 'y' and mass[8] == 'y':
        winy7 = True
        win2 = True
        pygame.draw.line(screen,green,[10,10],[290,290],4)
        return winy7,draw,win2
    if mass[2] == 'y' and mass[4] == 'y' and mass[6] == 'y':
        winxy8 = True
        win2 = True
        pygame.draw.line(screen,green,[290,10],[10,290],4)
        return winxy8,draw,win2
    if mass[0]!=''and mass[1]!=''and mass[2]!=''and mass[3]!=''and mass[4]!=''and mass[5]!=''and mass[6]!=''and mass[7]!=''and mass[8]!='':
        win = False
        draw = True
        return win,draw,win2
    else:
        win = False
        return win,draw,win2
def DrawWin(win,draw,win2,end):
    font = pygame.font.Font(None, 55)
    if win == True and win2 == False:
        font = pygame.font.Font(None, 40)
        text = font.render("Победа Крестиков",True,red)
        screen.blit(text,[25,120])
        print("Счёт 1 : 0")
    if win == True and win2 == True:
        font = pygame.font.Font(None, 40)
        text = font.render("Победа Ноликов",True,green)
        screen.blit(text,[30,120])
        print("Счёт 0 : 1")
    if draw == True and end == True:
        text = font.render("***** Ничья ****",True,blue)
        screen.blit(text,[10,140])
        print("Счёт 0 : 0")
        draw = False
        end = False
    return draw,end
def selection(even,odd,Flag1):
    xy2 = (0,0)
    font = pygame.font.Font(None, 44)
    text = font.render("Выберите X или O",True,green)
    screen.blit(text,[20,50])
    pygame.draw.rect(screen, black, [20,140, 105,100], 1)
    pygame.draw.rect(screen, black, [160,140, 105,100], 1)
    pygame.draw.rect(screen, white, [25,145, 95,90], 0)
    pygame.draw.rect(screen, white, [165,145, 95,90], 0)
    pygame.draw.line(screen,red,[30,150],[110,230],2)
    pygame.draw.line(screen,red,[30,230],[110,150],2)
    pygame.draw.circle(screen,green,[213,190],40,2)
    if event.type == pygame.MOUSEBUTTONDOWN and Flag == True:
        if event.button == 1:
            xy2 = event.pos
    x2 = xy2[0]
    y2 = xy2[1]
    if x2 > 20 and y2 > 140 and x2 < 125 and y2 < 240:
        screen.fill(gray)
        pygame.display.flip()
        even,odd = False,True
        Flag1 = True
    if x2 > 160 and y2 > 140 and x2 < 265 and y2 < 240:
        screen.fill(gray)
        pygame.display.flip()
        even,odd = True,False
        Flag1 = True
    return even,odd,Flag1
#*******************************
while done == False:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.display.flip()
    if win == False:
        if Flag1 == False:
            even,odd,Flag1 = selection(even,odd,Flag1)
        if Flag1 == True:
            DrawLine()
            xy,Flag2 = Cord(Flag,Flag1,Flag2)
            even,odd,mass = XoX(xy,even,odd,mass)
            win,draw,win2 = inspection(mass,draw,win2)
            draw,end = DrawWin(win,draw,win2,end)
        pygame.display.flip()
#*******************************
pygame.quit()
