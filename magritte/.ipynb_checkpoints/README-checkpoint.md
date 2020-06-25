```python
# ********************************************************************
# Conversation in the Clouds
# rOsita fu
# 2020-06-23
# github.com/atisor73
# ********************************************************************

def setup():
    global img
    size(800, 800)
    img = loadImage("magritte_conversation.png") # loading in image
    loadPixels()

def draw():
    global img
    background(255) 
    image(img,0,0) 

    for i in range(50000):
        # randomly choose 50,000 pixels from image
        x = int(random(img.width))
        y = int(random(img.height))
        loc = int(x + y*img.width)
        # retrieve color of pixel
        r,g,b = red(img.pixels[loc]),green(img.pixels[loc]),blue(img.pixels[loc])
        c = color(r,g,b)
        # then ellipse() draws a circle centered @ pixel 
        noStroke()
        fill(c) 
        size = random(5,13)
        ellipse(x, y, size,size)

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
    
```








