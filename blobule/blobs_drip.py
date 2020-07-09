# ********************************************************************
# BLOBULES -- drip variations
# rOsita fu
# 07-08-2020
# github.com/atisor73
# ********************************************************************
randomSeed(1234567)
noiseSeed(7654321)
save = False
loop = False
num_blobs = 2400
bg_color = (249, 234, 228)
width, height = 1000, 1000

def setup():
    size(width, height)
    if loop == False:
        noLoop()
    background(*bg_color)

# BLOB DRAWING FUNCTION **********************************************
def blob(center, colour, r_min, r_max, noise_max, phase, frame, speed, drip):
    translate(center[0], center[1])
    fill(colour)

    beginShape()
    for a in [PI/2+PI*_/100 for _ in range(100)]:
        off1 = map(cos(a+phase), -1, 1, 0, noise_max+phase)
        off2 = map(cos(a), -1, 1, 0, noise_max)
        r = map(noise(off1, off2), 0, 1, r_min, r_max)
        vertex(r*sin(a), r*cos(a))

    for a in [3*PI/2 + PI*_/100 for _ in range(100)]:
        off1 = map(cos(a+phase), -1, 1, 0, noise_max+phase)
        off2 = map(cos(a), -1, 1, 0, noise_max)
        r = map(noise(off1, off2), 0, 1, r_min, r_max)
        vertex(r*sin(a), 
               r*cos(a) + frame*speed *(10*exp(-0.001*drip/r_max*pow(abs(r*sin(a)), 2)))
               )
    endShape()
    translate(-center[0], -center[1])

# COLOR INTERPOLATION FUNCTION****************************************
def rgb_interpolation(colour1, colour2, fraction):
    """ colour1 (tuple): rgb
        colour2 (tuple): rgb """
    r1, g1, b1 = colour1[0], colour1[1], colour1[2]
    r2, g2, b2 = colour2[0], colour2[1], colour2[2]
    r = (r2-r1)*fraction + r1
    g = (g2-g1)*fraction + g1
    b = (b2-b1)*fraction + b1
    return (r, g, b)

# INSTANTIATION *******************************************************
# centers: pick a bunch of centers within a radius of the center 
# colours: pick a bunch of colors (custom palettes made in procreate)
# r_mins/r_maxs: pick blobbiness/spikiness of blobs
# frames, phases, off3s: offset movements 
centers = []
colours = []
r_mins, r_maxs = [], []
noise_maxs, phases = [], []
speeds, drips = [], []

# spikiness 
for _ in range(num_blobs):
    phases.append(random(0,5))                
    noise_maxs.append(random(2.5, 8.5))        
    if random(100) < 30:
        drips.append(random(500,1000))
    else:
        drips.append(random(10000,50000))

# sizes of blobs: some big some small
for _ in range(int(num_blobs)/2):
    r_mins.append(random(0, 5))
    r_maxs.append(random(r_mins[_], 90))
for _ in range(int(num_blobs)/2-1, num_blobs):
    r_mins.append(random(0, 5))
    r_maxs.append(random(r_mins[_], 20))

# drip speeds
min_speed, max_speed = 0.01, 2.0
min_r, max_r = min(r_mins), max(r_maxs)
for _ in range(num_blobs):
    __ = random(100)
    if __ < 10:
        speeds.append(map(random(r_mins[_], r_maxs[_]), min_r, max_r, 10.0, 0.0))
    elif __ < 20:
        speeds.append(map(random(r_mins[_], r_maxs[_]), min_r, max_r, 0.0, 0.01))
    else:
        speeds.append(map(random(r_mins[_], r_maxs[_]), min_r, max_r, min_speed, max_speed))

# centers of blobs: make bigger blobs in middle, smaller on edge
for _ in range(int(num_blobs)/2):
    _centerR = random(0, width/4+random(45))
    _centerA = random(0, 2*PI)
    centers.append((_centerR * cos(_centerA),
                    _centerR * sin(_centerA)))
for _ in range(int(num_blobs)/2-1, num_blobs):
    _centerR = random(width/5, width/3.5 + random(55))
    _centerA = random(0, 2*PI)
    centers.append((_centerR * cos(_centerA),
                    _centerR * sin(_centerA)))

# palette: rgb interpolate palette1 and palette2 w/ spatial dependency
palette2 = [(94,47,47), # anderson
            (222,182,182),
            (160,183,198),
            (46,52,64),
            (181,68,62),
            (121, 136, 129),
            (91, 84, 66),
            (236, 223, 205)
            # (219, 195, 121)
            ]
palette2 = [
            # (167, 113, 122),  # weird pastel
            # (128, 114, 132),
            # (56, 31, 47),
            # (141, 41, 46),
            # (84, 51, 49),

            (147, 93, 102),
            (108, 94, 112),
            (36, 11, 27),
            (121, 21, 26),
            (64, 31, 29),

            (252, 244, 238)
            ]
            # (225, 181, 143),
palette2 = [(254,89,89),  # really bright one
            (252,246,219),
            (73,143,151),
            (254,176,95),
            (27,58,84),
            (28, 11, 66)
            ]
palette2 = [(206, 216, 231),  # ipad background flower
            (23,31,45),
            (23,31,45),
            (64,78,102),
            (205, 170, 186),
            (150,86,115),
            (249, 234, 228) #bg
            ]
palette2 = [(142,0,76),      # ipad background squiggles
            (136,1,67),
            (0,9,82),
            (0,37,89),
            (249,231,227),
            (231,190,202)]

palette1 = [(251, 235, 234),(241, 210, 208),
            #(121, 75,102), 
            (158, 90, 107),
            (102, 51, 79),
            (52,34,60)

            ]

_ys = [center[1] for center in centers]
y_max = max(_ys)

# constructing palette
for _ in range(num_blobs):
    if True:
    # if random(1000) < 700:
        r,g,b = palette1[int(random(len(palette1)))]
        colours.append(color(r-40,g-40,b-40))
    else: # when visualizing 256 palettes, spatial dependence is vertical
        y_frac = map((centers[_][1] + random(-80, 80))/ y_max, -1.5, 1.5, 0.01, 0.99)
        i1 = int(y_frac * len(palette1))
        i2 = int((y_frac) * len(palette2))
        # i1, i2 = int(random(len(palette1))), int(random(len(palette2)))
        colour1 = palette1[i1]
        colour2 = palette2[i2]
        fraction = random(0,.1)
        r, g, b = rgb_interpolation(colour1, colour2, fraction)
        colours.append(color(r, g, b))

# new indices, drawing blobs out of order
original = [_ for _ in range(num_blobs)]
indices = []
while len(indices) != num_blobs:
    chosen = original[int(random(len(original)))]
    indices.append(chosen)
    original.remove(chosen)

frame = 0
t, t_switch, t_end = 0, 12, 24
reverse = False
# DRAWING ************************************************************
def draw():
    global centers, colours, r_mins, r_maxs, noise_maxs, phases
    global speeds, drips
    global frame, t, t_switch, t_end, reverse

    translate(width/2, height/2)
    noStroke()

    # ROTATION
    noise_maxs = [map(sin(frame/5), -1, 1, 2.5, 4.5)
                  for i in range(num_blobs)]

    # BLOBBIN
    for i in indices:
        blob( centers[i],
              colours[i],
              r_mins[i],
              r_maxs[i],
              noise_maxs[i],
              phases[i],
              frame,
              speeds[i],
              drips[i],
            )
    if reverse == True:
        frame -= 0.05
    else: 
        frame += 0.05
    t += 0.05
    if t > t_switch:
        reverse=True
    if t > t_end:
        noLoop()

    # GIFFIN'
    if save == True:
        project = "blobs_drip"
        output_dir = "../outputs/PNG_temps/"
        output_filename = os.path.join(
            output_dir, '{}_####.png'.format(project))
        saveFrame(output_filename)

#
#         .__....._                  _.....__,
#              .": o :':          ;': o :".
#              `. `-' .'.        .'. `-' .'
#                `---'              `---'
#     _...----...       ...   ...       ...----..._
#  .-'__..-""'----     `. `ρζ`  .'     ----'""-..__`-.
# '.-'   _.--"""'        `-._.-'        '"""--._   `-.`
# '  .-"'                   :                   `"-.  `
#   '   `.               _.'"'._               .'   `
#         `.        ,.-'"       "'-.,        .'
#           `.                            .'
#             `-._                   _.-'
#                 `"'--...___...--'"`'
#
# ********************************************************************




"""
notes:
speed of overall animation controlled by incrementation of frame
num_blobs controls sparseness
change noiseSeed and randomSeed for different patterns
change drip equation in vertex() line of blob function, 
    default is just a gaussian lookin thing
coeffecient in vertex equation in blob function controls sharpness of drops 
drips kinda randomzies this sharpness
updating noise_maxs gives the movement of blob edges/overall spikiness controlled by phase 

color interpolation is really for mixing palettes, never quite got that up to snuff
curent usage: mainly for palette visualizations
"""
