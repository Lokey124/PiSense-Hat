from sense_hat import SenseHat
import time

s = SenseHat()




s.low_light = True
s.set_rotation(270)

green = (124,252,0)
yellow = (255,215,0)
blue = (30,144,255)
pink = 	(255,192,203)
red = 	(255,0,0)
navy = 	(0,0,128)
beige = (255,228,196)
violet = (128,0,128)
grey = (128,128,128)
darkgrey = (105,105,105)
perwinkle = (147,112,219)
darkgreen = (0,100,0)
brown = (139,69,19)
peach = (210,105,30)
black = (0,0,0)
white = (255,255,255)
snow = 	(255,250,250)
maroon = (128,0,0)
thistle = (216,191,216)
nothing = (0,0,0)

def scrooge_logo():
    
    Y = yellow
    B = blue
    D = black
    R = red
    N = navy
    V = violet
    A = grey
    P = perwinkle
    Z = brown
    W = white
    O = nothing
    logo = [
    O, O, O, P, N, N, O, O,
    O, O, O, R, V, V, O, O,
    O, O, N, N, N, N, N, O,
    O, O, P, W, D, W, O, O,
    A, O, W, Y, Y, Y, Y, O,
    R, B, B, R, V, N, V, P,
    W, A, B, W, P, O, O, V,
    Y, R, O, Z, V, Z, O, V,
    ]
    return logo

def huey_logo():
    
    R = red
    W = white
    E = maroon
    Y = yellow
    V = violet
    A = grey
    J = peach
    D = black
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, R, R, O, O, O,
    O, O, R, W, W, E, O, O,
    O, O, W, D, W, D, O, O,
    O, O, Y, Y, Y, Y, Y, O,
    W, R, R, E, O, O, O, O,
    O, W, R, A, O, O, O, O,
    Y, Y, O, J, J, O, O, O,
    ]
    return logo

def duey_logo():
    
    B = blue
    W = white
    Y = yellow
    D = black
    J = peach
    P = perwinkle
    A = grey
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, B, B, O, O, O,
    O, O, B, W, W, P, O, O,
    O, O, W, D, W, D, O, O,
    O, O, Y, Y, Y, Y, Y, O,
    W, B, B, P, O, O, O, O,
    O, W, B, A, O, O, O, O,
    Y, Y, O, J, J, O, O, O,
    ]
    return logo

def luey_logo():
    G = green
    L = darkgreen
    W = white
    Y = yellow
    J = peach
    D = black
    A = grey
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, G, W, W, L, O, O,
    O, O, W, D, W, D, O, O,
    O, O, Y, Y, Y, Y, Y, O,
    W, G, G, L, O, O, O, O,
    O, W, G, A, O, O, O, O,
    Y, Y, O, J, J, O, O, O,
    ]
    return logo

def launchpad_logo():
    Z = brown
    Y = yellow
    D = black
    X = pink
    V = violet
    P = perwinkle
    K = darkgrey
    H = beige
    U = thistle
    W = white
    O = nothing
    logo = [
    O, O, O, Z, W, Y, Y, Y,
    H, O, O, W, D, W, D, O,
    O, H, H, Y, Y, Y, Y, Y,
    O, Z, Z, Y, Y, X, X, O,
    Z, O, Z, V, Y, Y, Y, V,
    W, O, O, Z, V, V, O, P,
    O, O, U, U, Z, Z, Z, O,
    O, K, K, O, O, O, V, V,
    ]
    return logo

images = [scrooge_logo, huey_logo, duey_logo, luey_logo, launchpad_logo,]
count = 0

while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(2)
    count += 1    
