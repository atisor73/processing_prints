# ********************************************************************
# ROTATIONS IN RED AND BLACK -- found algorithm to recreate original!
# rOsita fu
# 06-23-2020
# github.com/atisor73
# ********************************************************************

def setup():
    size(800,800)
    noLoop()

rows, cols = 10, 10 # rows and cols of lines
l = 23 #line_length line_length

ang = []
for i in range(rows/2):
    ang_ = []
    for j in range(cols/2):
        # shift = i*j*PI/18
        shift = (i%7)*(j%7)*PI/5
        ang_.append(PI/4-shift)
    [ang_.append(a) for a in ang_[::-1]]
    ang.append(ang_)
[ang.append(a) for a in ang[::-1]]

def draw():
    background(240, 231, 219)
    global rows, cols, ang, t
    strokeWeight(6)

    for i in range(rows):
        for j in range(cols):
            sgn = pow(-1, i+j)
            centerx = i/1.5*width/cols + width/10 + 50
            centery = j/1.5*height/rows + height/10 +50
            
            stroke(18,19,10)
            line(centerx + sgn*l*cos(ang[i][j]), 
                 centery + l*sin(ang[i][j]), 
                 centerx - sgn*l*cos(ang[i][j]), 
                 centery - l*sin(ang[i][j]))
            
            stroke(148,49,56)
            line(centerx - sgn*l*sin(ang[i][j]),
                centery + l*cos(ang[i][j]),
                centerx + sgn*l*sin(ang[i][j]),
                centery - l*cos(ang[i][j]))


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
