import sys
import pygame as pg


class Surface_Editor():
    
    def __init__():
        pass
    
    def fill(surface, color):
     """Fill all pixels of the surface with color, preserve transparency."""
     w, h = surface.get_size()
     r, g, b, _ = color
     for x in range(w):
         for y in range(h):
             a = surface.get_at((x, y))[3]
             surface.set_at((x, y), pg.Color(r, g, b, a))