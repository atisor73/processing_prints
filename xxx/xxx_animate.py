# ********************************************************************
# ROTATIONS IN RED AND BLACK -- variations in motion
# rOsita fu                 
# 2020-06-23               
# github.com/atisor73       
# ********************************************************************

def setup():
    size(800, 800)


rows, cols = 10, 10  # rows and cols of lines
l = 23  # line_length line_length

ang = []
for i in range(rows/2):
    ang_ = []
    for j in range(cols/2):
        shift = (i%5+0.02)*(j%5+0.02)*PI/6.2      # VARIATIONS IN CUSTOMIZING SHIFT
        ang_.append(PI/4-shift)
    [ang_.append(a) for a in ang_[::-1]]
    ang.append(ang_)
[ang.append(a) for a in ang[::-1]]

t = [[0.0 for _ in range(cols)] for _ in range(rows)]
firstrun = True


def draw():
    background(240, 231, 219)
    global rows, cols, ang, t, firstrun
    strokeWeight(6)

    ang = [[ang[i][j] + 0.08*pow(sin(t[i][j]),3)
            for j in range(cols)] for i in range(rows)]

    ### PING PONG LOOPING
    # if t[0][0] < 0:
    #     t = [[-0.00001 for _ in range(cols)] for _ in range(rows)]
    # if t[0][0] < 11 and firstrun:
    #     t = [[t[i][j] + 0.02 for j in range(cols)] for i in range(rows)]
    # else:
    #     t = [[t[i][j] - 0.025 for j in range(cols)] for i in range(rows)]
    #     firstrun = False
    t = [[t[i][j] + 0.02 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            sgn = pow(-1, i+j)
            centerx = i/1.5*width/cols + width/10 + 75
            centery = j/1.5*height/rows + height/10 + 75

            stroke(18, 19, 10)
            line(centerx + sgn*l*cos(ang[i][j]),
                 centery + l*sin(ang[i][j]),
                 centerx - sgn*l*cos(ang[i][j]),
                 centery - l*sin(ang[i][j]))

            stroke(148, 49, 56)
            # line(centerx - sgn*l*sin(ang[i][j]),
            #      centery + l*cos(ang[i][j]),
            #      centerx + sgn*l*sin(ang[i][j]),
            #      centery - l*cos(ang[i][j]))
            line(centerx - sgn*l*cos(ang[i][j]),
                 centery + l*sin(ang[i][j]),
                 centerx + sgn*l*sin(ang[i][j]),
                 centery - l*sin(ang[i][j]))





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
