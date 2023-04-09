INF = 1E10


def dot(v1, v2):
    return (v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2])

def cross(v1, v2):
    pass

def vector_ab(a,b):
    return (b[0]-a[0] , b[1]-a[1], b[2]-a[2])

def vector_len(a):
    return (a[0]*a[0]+a[1]*a[1]+a[2]*a[2])**0.5

def vector_sum(a,b):
    return (b[0]+a[0] , b[1]+a[1], b[2]+a[2])

def vector_scale(a,t):
    b = [a[i] for i in range(len(a))]
    for i in range(len(a)):
        b[i] *= t
    return b

def vector_normalize(a):
    b = [a[i] for i in range(len(a))]
    t = vector_len(a)
    for i in range(len(a)):
        b[i] *= t
    return b