# ********************************************************************
# rOsita fu
# 06-23-2020
# github.com/atisor73
# ********************************************************************

save = True
def setup():
    size(500, 700)
    frameRate(10)

rows, cols = 15, 15
num_squares = rows*cols

t = [random(10) for i in range(num_squares)]
stretch = [random(3, 7) for i in range(num_squares)]

# choosing random squares
chosen = []
for i in range(rows):
    chosen_row = []
    for j in range(cols):
        if int(random(0.7, 1.99)) == 0:
            chosen_row.append(0)
        else:
            chosen_row.append(1)
    chosen.append(chosen_row)

# bacon lorem ipsum, and political lorem ipsum
words = """Bacon ipsum dolor amet frankfurter salami ball tip drumstick leberkas hamburger. Boudin chuck capicola pork belly. Porchetta strip steak cupim, ham tail burgdoggen shankle sausage ham hock pork chop pork. Picanha flank tri-tip chicken, prosciutto capicola pig sirloin bresaola pastrami swine sausage pancetta spare ribs. Beef pork chop capicola, flank cow spare ribs chuck ham salami. Burgdoggen ham hock porchetta, pastrami turkey shank alcatra buffalo hamburger chislic strip steak drumstick beef capicola cupim. Sausage filet mignon ground round cupim pork chop, shoulder pork salami meatball. Frankfurter tail salami doner filet mignon short loin ground round cupim fatback shankle strip steak ball tip pancetta tongue. Tri-tip sausage drumstick tenderloin rump kielbasa turducken. Kielbasa ham turducken shankle, porchetta ham hock brisket spare ribs pork chop shoulder doner. Chicken shoulder burgdoggen meatball cupim buffalo jowl turkey short loin capicola boudin pork belly."""
words = """For over a thousand years, Al-Azhar becaon of Islamic learning. Egypt's advancement Buchenwald, a network of camps where reverends were enslaved, tortured, and shot. Countries grew their economoies while maintaining distinct cultures. Waded into battles over prison reform and temperance, above all, abolition. Speak as clearly and plainly as I can. Thank you. Change tax code lobbyists station. Live communities power in mosques, temples, synagogues. Nuclear elections share common principles of justice and progress, tolerance and dignity of all human beings. Offensive sexuality and mindless violence, the internet and television can bring. Source of advancement, faith, daughters contribute and gather. Preparing to divide, pledge our allegiance, and race with bombings. Race, criminal systems emerging church of aggression knocking at the very source of administrative duties. March into the future, WAR takien to the Palestinian lives, civilians, real evil, hardship, and suffering plague. Government court justices can fail to explain the pledging, the verge of helpless poverty. Unemployment plans particularly tricky of the type"""


def draw():
    global rows, cols, stretch, t, num_squares, chosen  # setting global variables
    background(color(204, 196, 181))  # color of paper

    # DRAWING LETTERS ----------------------------------------------
    # f = createFont("1942.ttf",25)
    f = createFont("AmericanTypewriter-Condensed", 25)
    textFont(f)
    # textSize(25)
    textSize(20)
    fill(0)
    start = 0
    end = start + 50
    for i in range(rows+1):
        text(words[start: end], 10, i*height/rows+35)
        start = end
        end += 75

    # DRAWING BOXES --------------------------------------------------
    noStroke()  # no outline for boxes
    stretch = [stretch[i] + sin(40*t[i])
               for i in range(num_squares)]  # width of boxes
    t += [t[i] + 2*PI/400 for i in range(num_squares)]  # advance in time
    for i in range(rows):
        for j in range(cols):
            if chosen[i][j] == 1:
                # randomize 'redness' of square colors
                fill(int(random(140, 170)), int(
                    random(0, 10)), int(random(0, 10)))
                index = j+i*rows
                centerx = i*width/cols + width/25
                centery = j*height/rows + height/25

                x1, y1 = centerx-stretch[index], centery-8+int(random(4))
                x2, y2 = centerx-stretch[index], centery+8+int(random(4))
                x3, y3 = centerx+stretch[index], centery+8+int(random(4))
                x4, y4 = centerx+stretch[index], centery-8+int(random(4))
                quad(x1, y1, x2, y2, x3, y3, x4, y4)


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
