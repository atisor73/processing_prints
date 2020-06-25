# ********************************************************************
# rOsita fu
# 06-23-2020
# github.com/atisor73
# ********************************************************************
save = True # saving frames for .mov or .gif purposes

def setup():
    size(900, 900)
    frameRate(10)

rows, cols = 50, 50 # 15, 15
num_squares = int(rows*cols)

t = [random(10) for i in range(num_squares)]
stretch = [random(-1,1) for i in range(num_squares)]

def draw():
    global rows, cols, stretch, t, num_squares  # setting global variables
    background(color(204, 196, 181)) # color of paper
    
    # DRAWING BOXES
    noStroke()  # no outline for boxes
    stretch = [stretch[i] - random(-1*abs(-2+t[i]/50), abs(1.8-t[i]/50)) * sin(10*t[i])
                for i in range(num_squares)] # width of boxes
    t = [t[i] + 2*PI/10 for i in range(num_squares)] # advance in real time 
    for i in range(rows):
        for j in range(cols):
            index = j+i*cols

            centerx = i/1.5*width/cols + width/10 + 75
            centery = j/1.5*height/rows + height/10 + 75
            # x1, y1 = centerx-stretch[index], centery-18+int(random(4))
            # x2, y2 = centerx-stretch[index], centery+18+int(random(4))
            # x3, y3 = centerx+stretch[index], centery+18+int(random(4))
            # x4, y4 = centerx+stretch[index], centery-18+int(random(4))
            x1, y1 = centerx-stretch[index], centery-8+int(random(4))
            x2, y2 = centerx-stretch[index], centery+8+int(random(4))
            x3, y3 = centerx+stretch[index], centery+8+int(random(4))
            x4, y4 = centerx+stretch[index], centery-8+int(random(4))

            fill(190, 133, 118) # shadow color
            quad(x1+5, y1+5, x2+5, y2+5, x3+5, y3+5, x4+5, y4+5) # shadow?

            ### RED RED
            # fill(int(random(130+stretch[index], 170)),
            #      int(random(0, 10)), int(random(0, 10)))

            ### DARKER RED
            fill(int(random(110+stretch[index], 140)),
                 int(random(20, 40)), int(random(20, 40)))

            ### MULTIPLE COLORS
            # fill(int(random(110+stretch[index], 140)),
            #      int(random(20, 40)), int(random(30, 80)))
            
            quad(x1, y1, x2, y2, x3, y3, x4, y4)

    if save == True:
        project = "red_ppl"
        output_dir = "../outputs/PNG_temps/" 
        output_filename = os.path.join(output_dir, '{}_####.png'.format(project))
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
