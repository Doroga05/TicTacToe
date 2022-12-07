import pygame as p 

Swidth = 300
Sheight = 300
p.init()
screen = p.display.set_mode((Swidth,Sheight))
p.display.set_caption("Tic Tac Toe (Ts)")
klocka = p.time.Clock()

#Pre Def
done = False
line_width = 6
Markers = []
clicked = False
pos = []
player = 1

#color
G = 0, 255, 0
R = 255, 0 , 0


def Dgrid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for TS in range (1,3):
        p.draw.line(screen, grid, (0, TS * 100), (Swidth, TS * 100), line_width)
        p.draw.line(screen, grid, (TS * 100, 0), (TS * 100, Sheight), line_width)

def Dmarkers():
    x_pos = 0
    for TS in Markers:
        y_pos = 0
        for y in TS:
            if y == 1:
                p.draw.line(screen, G, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                p.draw.line(screen, G, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                p.draw.circle(screen, R, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1



#Spelplanen (datorns sida)
for TS in range(3):
    Row = [0] * 3
    Markers.append(Row)
print(Markers)


#Main Game Loop
while(done == False):
    Dgrid()
    Dmarkers()

   #EVENTS
    for event in p.event.get():
        #quit
        if(event.type == p.QUIT):
            done = True
        if event.type == p.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == p.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = p.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if Markers[cell_x // 100][cell_y // 100] == 0:
                Markers[cell_x // 100][cell_y // 100] = player
                player *= -1
        print(Markers)

    p.time
 

    #Rita alla förändringar.
    p.display.update()

p.quit()