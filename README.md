# 3D_rotating_cube_pygame
![Cube](https://github.com/jimmyahalpara/3D_rotating_cube_pygame/blob/master/ezgif.com-optimize.gif)
In this code I have used pygame to draw a 3d rotating cube. The main challenge in this program is to draw 3d on 2d screen, that is pygame,is a 2d but in our case the coordinates of the cube are in 3d that is, x,y,z. So our main objective of the code is to convert the x,y,z coordinates to 2d x,y.
Following code block will do this job in our program.


```python
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
```

This return_rendered_point will take points (x,y,z), and viewing distance and return (x,y) coordinates. This function will also use three extra variables that is self.rotx, self.roty, self.rotz which stores the rotation angle for the three axis.
Another challenge is the fill colors to the sides, we can use polygon method of the pygame to do that, but the hard thing is to print all the polygons in order so that, the polygon which is near to the screen or camara in 3d space should be printed at last on all other polygons and polygon far from screen should be printed first. 
This problem can be solved by sorting the list containg the polygon objects in decreasing order of their length from polygons midpoint to the position, at middle of the screen.
The distance is calculated by the following function,


```python
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
```

and the sorting thig is done by following method..


```python
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
```
