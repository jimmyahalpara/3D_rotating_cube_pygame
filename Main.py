#made by Jimmy Kumar Ahalpara
import pygame
from pygame.locals import *
pygame.init()
from math import *
h = 600
w = 900
centre = [w/2,h/2]
screen = pygame.display.set_mode((w,h))
class Cube:
    def __init__(self,position,vel = [0,0,0],rotx = 0,roty = 0, rotz = 0, points = [], edges = [], sides = [],ang_vel = [0,0,0],edge_color = (255,255,255), side_color = (0,0,0)):
        self.pos = position[:]
        self.vel = vel
        self.rotx = rotx
        self.roty = roty
        self.rotz = rotz
        self.ang_vel = ang_vel
        self.points = points
        self.edges = edges
        self.sides = sides
        self.edge_color = edge_color
        self.side_color = side_color
    def add_rotation(self,rotx = None,roty = None, rotz = None, ang_vel = None,):
        if rotx!=None:
            self.rotx = rotx
        if roty!=None:
            self.roty = roty
        if rotz!=None:
            self.rotz = rotz
        if ang_vel!= None:
            self.ang_vel = ang_vel
    def add_velosity(self,vel):
        x,y,z = vel
        self.vel = vel[:]
    def update(self):
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
        self.pos[2]+=self.vel[2]
        self.rotx+=self.ang_vel[0]
        self.roty+=self.ang_vel[1]
        self.rotz+=self.ang_vel[2]
    def update_color(self,edge_color = None, side_color = None):
        if edge_color!= None:
            self.edge_color = edge_color
        if side_color!= None:
            self.side_color = side_color
    def update_coordinates(self,position = None, points = None, edges = None, sides = None):
        if posiiton!=None:
            self.pos = position
        if points!= None:
            self.points = points
        if edges!= None:
            self.edges = edges
        if sides!= None:
            self.sides = sides
    def return_rendered_point(self,points,viewing_distance = 320):
        global centre
        x,y,z = points
        x,y=x*cos(radians(self.rotz))-y*sin(radians(self.rotz)),y*cos(radians(self.rotz))+x*sin(radians(self.rotz))
        y,z=y*cos(radians(self.rotx))-z*sin(radians(self.rotx)),z*cos(radians(self.rotx))+y*sin(radians(self.rotx))
        x,z=x*cos(radians(self.roty))-z*sin(radians(self.roty)),z*cos(radians(self.roty))+x*sin(radians(self.roty))
        x+= self.pos[0] - centre[0]
        y+= self.pos[1] - centre[1]
        z+= self.pos[2]
        x = x*viewing_distance/z
        y = y*viewing_distance/z
        x += centre[0]
        y += centre[1]
        return (int(x),int(y))
    def return_sort_meth(self,obj):
        global centre
        sx,sy,sz = 0,0,0
        for a in obj[0]:
            x,y,z = self.points[a]
            x,y=x*cos(radians(self.rotz))-y*sin(radians(self.rotz)),y*cos(radians(self.rotz))+x*sin(radians(self.rotz))
            y,z=y*cos(radians(self.rotx))-z*sin(radians(self.rotx)),z*cos(radians(self.rotx))+y*sin(radians(self.rotx))
            x,z=x*cos(radians(self.roty))-z*sin(radians(self.roty)),z*cos(radians(self.roty))+x*sin(radians(self.roty))
            x+= self.pos[0]
            y+= self.pos[1]
            z+= self.pos[2]
            sx+= x; sy += y; sz += z
        cp = [centre[0],centre[1],0]
        sx/=len(obj[0]);sy/=len(obj[0]);sz/=len(obj[0])
        dis = sqrt(((cp[0]-sx)**2)+((cp[1]-sy)**2)+((cp[2]-sz)**2))
        return dis
    def draw_cube(self,screen,show_edges = True):
        if show_edges:
            list1 = self.sides[:]
            list1.sort(key = self.return_sort_meth,reverse = True)
            for ab in list1:
                p =[]
                for a in ab[0]:
                    p.append(self.return_rendered_point(self.points[a]))
                pygame.draw.polygon(screen, ab[1],p)
            for b in self.edges:
                pygame.draw.line(screen,self.edge_color,self.return_rendered_point(self.points[b[0]]),self.return_rendered_point(self.points[b[1]]),1)
        else:
            list1 = self.sides[:]
            list1.sort(key = self.return_sort_meth,reverse = True)
            for ab in list1:
                p =[]
                for a in ab[0]:
                    p.append(self.return_rendered_point(self.points[a]))
                pygame.draw.polygon(screen, ab[1],p)
points = [(-100,-100,100),(-100,100,100),(100,100,100),(100,-100,100),(-100,-100,-100),(-100,100,-100),(100,100,-100),(100,-100,-100)]
edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
sides = [((0,1,2,3),(200,0,0)),((4,5,6,7),(0,200,0)),((0,4,7,3),(0,0,200)),((1,2,6,5),(100,100,100)),((0,1,5,4),(200,100,200)),((3,7,6,2),(100,200,200))]
cube = Cube([450,300,400],points = points, edges= edges,ang_vel = [0.25,0.085,0.042], side_color = (100,100,255), sides = sides)
#n = 0
while True:
    screen.fill((0,0,0))
    cube.update()
    cube.draw_cube(screen,show_edges = False)
    for event in pygame.event.get():
        if event.type == QUIT: pygame.quit()
    key = pygame.key.get_pressed()
    if key[K_a]: cube.rotz +=0.5
    if key[K_d]: cube.rotz -=0.5
    if key[K_s]: cube.rotx +=0.5
    if key[K_w]: cube.rotx -=0.5
    if key[K_q]: cube.roty +=0.5
    if key[K_e]: cube.roty -=0.5
    if key[K_LEFT]: cube.pos[0] -=0.5
    if key[K_RIGHT]: cube.pos[0] +=0.5
    if key[K_UP]: cube.pos[1] -=0.5
    if key[K_DOWN]: cube.pos[1] +=0.5
    #pygame.image.save(screen, "screenshot"+str(n)+".jpeg")
    #n+=1
    pygame.display.update()
