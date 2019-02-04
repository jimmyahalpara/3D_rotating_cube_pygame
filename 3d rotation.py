import pygame
from pygame.locals import *
from math import *
pygame.init()
h = w = 800
centre = [w/2,h/2]
radx = 0
rady = 0
radz = 0
pos = [400,400,101]
screen = pygame.display.set_mode((w,h))
pygame.mouse.set_visible(0);pygame.event.set_grab(1)
def return_rendered_point(points,viewing_distance=30):
    global centre, radx, rady, radz
    x,y,z = points
    x,y=x*cos(radx)-y*sin(radx),y*cos(radx)+x*sin(radx)
    y,z=y*cos(rady)-z*sin(rady),z*cos(rady)+y*sin(rady)
    x,z=x*cos(radz)-z*sin(radz),z*cos(radz)+x*sin(radz)
    x+= pos[0] - centre[0]
    y+= pos[1] - centre[1]
    z+= pos[2]
    x = x*viewing_distance/z
    y = y*viewing_distance/z
    x += centre[0]
    y += centre[1]
    return (int(x),int(y))

class Cube:
    def __init__(self):
        self.print_con = True
        self.color = (255,0,0)
        self.side_color = (255,150,200)
        self.size = [100,100,100]
        
    def update(self):
        if self.print_con:
            if self.typ == 'bullet':
                self.pos[1]-=0.75
            if self.typ == 'enemy':
                self.pos[1]+=0.1
            if self.typ == 'random':
                if self.side == 1:
                    self.pos[0]+=self.vel
                elif self.side == 2:
                    self.pos[0] -= self.vel
    def draw_cube(self,canvas):
        global pos
        self.pos = pos[:]
        point1 = [-self.size[0],-self.size[1],-self.size[2]]
        point2 = [-self.size[0],+self.size[1],-self.size[2]]
        point3 = [+self.size[0],+self.size[1],-self.size[2]]
        point4 = [+self.size[0],-self.size[1],-self.size[2]]
        point5 = [-self.size[0],-self.size[1],+self.size[2]]
        point6 = [-self.size[0],+self.size[1],+self.size[2]]
        point7 = [+self.size[0],+self.size[1],+self.size[2]]
        point8 = [+self.size[0],-self.size[1],+self.size[2]]
        edges = [(point1,point2),(point2,point3),(point3,point4),(point4,point1),(point5,point6),(point6,point7),(point7,point8),(point8,point5),
        (point1,point5),(point2,point6),(point3,point7),(point4,point8)]
        sides = [(point1,point2,point3,point4),(point5,point6,point7,point8),(point1,point4,point8,point5),(point2,point3,point7,point6),(point1,point2,point6,point5),(point7,point8,point4,point3)]
        for vertice in sides:
            pygame.draw.polygon(screen,(100,100,255),(return_rendered_point(vertice[0]),return_rendered_point(vertice[1]),return_rendered_point(vertice[2]),return_rendered_point(vertice[3])))
        for edge in edges:
            pygame.draw.line(screen,(255,255,255),return_rendered_point(edge[0]),return_rendered_point(edge[1]),1)
l = Cube()
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT: pygame.quit()
    key = pygame.key.get_pressed()
    if key[K_a]: pos[0]-=1.0
    if key[K_d]: pos[0]+=1.0
    if key[K_w]: pos[1]-=1.0
    if key[K_s]: pos[1]+=1.0
    if key[K_q]: pos[2]-=1.0
    if key[K_e]: pos[2]+=1.0
    if key[K_ESCAPE]: pygame.quit()
    k = pygame.mouse.get_rel()
    radz+= k[0]/1000.0
    rady+= k[1]/1000.0
    l.draw_cube(screen)
    pygame.display.update()
