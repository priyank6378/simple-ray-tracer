
class Canvas : 
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self._canvas = [[(0,0,0) for i in range(w)] for j in range(h)]

    def putPixel(self, x, y, color):
        c = [int(i) for i in color]
        self._canvas[x][y] = c

    def get_canvas(self):
        return self._canvas
    
