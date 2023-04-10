from models import Sphere
from light import LightSource
from canvas import Canvas
from utils import *
import matplotlib.pyplot as plt

s1 = Sphere(1 , (0,-1,3), (255,0,0), 500)
s2 = Sphere(1, (2,0,4), (0,0,255), 500)
s3 = Sphere(1, (-2,0,4), (0,255,0), 10)
s4 = Sphere(5000, (0, -5001, 0), (255,255,0), 1000)
spheres = [s1,s2,s3,s4]

lights = [
    LightSource("ambient",0.2),
    LightSource("point", 0.6, (2,1,0)),
    LightSource("directional", 0.2, (1,4,4))
]

BACKGROUND_COLOR = (255,255,255)

Wv = 1  # width of viewport
Hv = 1  # height of viewport
viewport_size = (Wv, Hv)
projection_plane_d = 1

camera_loc = (0,0,0)

canvas = Canvas(1000,1000)


def canvasToViewPort(x, y):
    return (x*Wv/canvas.w , y*Hv/canvas.h, projection_plane_d)


def objectFound(o, d, l , h):
    nearest_obj = None
    color = BACKGROUND_COLOR
    nearest_point = INF
    for obj in spheres:
        t1, t2 = obj.intersectionPoints(o, d) # op = o + t*d    
        if (t1>=l and t1<=h and t1<nearest_point):
            nearest_point = t1
            nearest_obj = obj
            color = obj.color
        if (t2>=l and t1<=h and t2<nearest_point):
            nearest_obj = obj
            color = obj.color
            nearest_point = t2

    if (nearest_obj == None) :
        return color
    P = vector_sum(o , vector_scale(d, nearest_point))
    N = vector_ab(nearest_obj.center, P)
    N = vector_normalize(N)
    color = vector_scale(color , computeLightining(P,N, vector_scale(d, -1), nearest_obj.s))

    return color

def computeLightining(P, N, V, s):
    i = 0
    for light in lights:
        if light.type == "ambient":
            i += light.i
        else :
            if light.type == "point":
                L = vector_ab(P, light.coordinates)
                t_max = 1
            else :
                L = light.coordinates
                t_max = INF
                
            color = objectFound(P, L, 0.001, t_max)
            if (color != BACKGROUND_COLOR): # if object in shadow we skip adding diffuse and specular
                continue

            # diffuse
            n_dot_l = dot(N, L)
            if n_dot_l>0:
                i += light.i * n_dot_l/(vector_len(N)*vector_len(L))

            # specular
            if s!=-1:
                R = vector_ab(L, vector_scale(N, 2*dot(N,L)))
                r_dot_v = dot(R,V) 
                if r_dot_v>0:
                    i += light.i * pow(r_dot_v/(vector_len(R) * vector_len(V)) , s)
    return i


# main loop
for x in range(-canvas.w//2, canvas.w//2):
    for y in range(-canvas.h//2, canvas.h//2):
        D = canvasToViewPort(x,y)   
        found_color = objectFound(camera_loc, D, 1, INF)
        canvas.putPixel(x+canvas.w//2,canvas.h//2+y,found_color)
        
plt.imshow(canvas.get_canvas())
plt.show()