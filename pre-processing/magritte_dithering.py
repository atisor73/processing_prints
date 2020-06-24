# ********************************************************************
# rOsita fu
# 2020-06-23
# github.com/atisor73
# ********************************************************************
def setup():
    global img
    size(800, 800)
    img = loadImage("magritte_conversation.png")
    loadPixels()

def draw():
    global img
    background(255)
    image(img,0,0)
    for i in range(50000):
        x = int(random(img.width))
        y = int(random(img.height))
        loc = int(x + y*img.width)
        r,g,b = red(img.pixels[loc]),green(img.pixels[loc]),blue(img.pixels[loc])
        c = color(r,g,b)
        noStroke()
        fill(c)
        ellipse(x, y, 10,10)


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



    









