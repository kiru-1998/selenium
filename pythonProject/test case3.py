
from sketchpy import canvas
from turtle import screensize
s=screensize()
s.("Black")
ab=canvas.sketch_from_svg('LordShiva/shivji.svg', scale=45)
ab.draw()
