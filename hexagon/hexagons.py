
save = False
loop = True
frame_rate = 1

# ************************ CONSTANTS ***********************
width, height = 1200, 700
paddingx, paddingy = 100, 100

r = 24

palette = ["#D8862E", "#C54927", "#558F6A",
           "#DBAE4B","#9EAA3F","#373D44","#95A99B"]
bg_color = "#E4E1CF"
dark_color = "#373D44"
n_edges = 1800
threshold_color = 0.01 # how many colors change each iteration

# ************************ FUNCTIONS ***********************
def find_edge_map(edges):
    _delta = r * cos(PI/3.0)
    map = {}
    for edge in edges:
        p1, p2 = edge
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            candidates = [ ((x1, y1), (x2, y2)),
                            ((x1, y1), (x2, y2)),
                            ((x1, y1), (x2, y2)),
                            ((x1, y1), (x2, y2)),
                            ((x1, y1), (x2, y2)),
                            ((x1, y1), (x2, y2)),
                            ((x1, y1), (x2, y2)),
                            ((x1, y1), (x2, y2)),
                          ((x1, max(y1, y2)), (x1-a, max(y1, y2)+_delta)),
                          ((x1, max(y1, y2)), (x1+a, max(y1, y2)+_delta)),
                          ((x1, min(y1, y2)), (x1-a, min(y1, y2)-_delta)),
                          ((x1, min(y1, y2)), (x1+a, min(y1, y2)-_delta))
                         ]
        else:
            if y1 == max(y1, y2): x_bottom, x_top = x1, x2
            if y2 == max(y1, y2): x_bottom, x_top = x2, x1
            candidates = [ ((x_bottom, max(y1, y2)), (x_bottom, max(y1, y2)+r)),
                           ((x1, y1), (x2, y2)),
                           ((x1, y1), (x2, y2)),
                           ((x1, y1), (x2, y2)),
                           ((x1, y1), (x2, y2)),
                        ]
        within = []
        for candidate in candidates:
            p1, p2 = candidate
            x1, y1 = p1
            x2, y2 = p2
            if (x1 < a) or (x2 < a):
                pass
                x1 += 2*a*(n_cols-1)
                x2 += 2*a*(n_cols-1)
            elif (x1 > 2*a*(n_cols)) or (x2 > 2*a*(n_cols)):
                x1 -= 2*a*(n_cols-1)
                x2 -= 2*a*(n_cols-1)
            elif (y1 > (3*(n_rows)+2)/2.0 * r) or (y2 > (3*(n_rows)+2)/2.0 * r):
                y1 -= (3/2.0) * r * n_cols
                y2 -= (3/2.0) * r * n_cols
            within.append(((x1, y1), (x2, y2)))
        map[edge] = within
    return map

def find_new_edges(edges, map):
    new_edges = []
    for edge in edges:
        index = int(random(len(map[edge])))
        new_edge = map[edge][index]
        new_edges.append(new_edge)
    return new_edges

# ******************** BUILDING ARRAYS *********************
a = r*cos(PI/6.0)
n_rows = int((height-2.0*paddingy)/(1.5*r))
n_cols = int((width-2.0*paddingx)/(2.0*a))

center_xs, center_ys = [], []
for i in range(n_rows):
    if i % 2 == 1: center_xs.append([2*j*a for j in range(n_cols)])
    else: center_xs.append([(1+(2*j))*a for j in range(n_cols-1)])
    center_ys.append([ (3*i + 2)/2.0*r for _ in range(n_cols)])

colors = []
edges = []
for xrow, yrow in zip(center_xs, center_ys):
    for x, y in zip(xrow, yrow):
        colors.append(palette[int(random(len(palette)))])
        edges.extend( [((x, y-r),      (x+a, y-r/2.0)),
                      ((x+a, y-r/2.0), (x+a, y+r/2.0)),
                      ((x+a, y+r/2.0), (x, y+r)),
                      ((x, y+r),       (x-a, y+r/2.0)),
                      ((x-a, y+r/2.0), (x-a, y-r/2.0))]
                    )
chosen_edges = []
for _ in range(n_edges):
    index = int(random(len(edges)))
    chosen_edges.append(edges[index])
edge_map = find_edge_map(chosen_edges)

# ************************ DRAWING ***********************
def setup():
    size(width, height)
    if loop == False: noLoop()
    frameRate(frame_rate)

def draw():
    global chosen_edges, edge_map

    translate(paddingx+1.5*r, paddingy)
    background(bg_color)

    # filling hexagons .................................
    c = 0
    for xrow, yrow in zip(center_xs, center_ys):
        for x, y in zip(xrow, yrow):
            noStroke()
            if random(1) < threshold_color:
                colors[c] = palette[int(random(len(palette)))]
            fill(colors[c])
            beginShape()
            vertex(x, y-r)
            vertex(x+a, y-r/2.0)
            vertex(x+a, y+r/2.0)
            vertex(x, y+r)
            vertex(x-a, y+r/2.0)
            vertex(x-a, y-r/2.0)
            endShape()
            c += 1

    # bg_color borders ..................................
    for xrow, yrow in zip(center_xs, center_ys):
        for x, y in zip(xrow, yrow):
            stroke(bg_color)
            strokeCap(ROUND)
            strokeWeight(2.0)
            noFill()

            beginShape()
            vertex(x, y-r)
            vertex(x+a, y-r/2.0)
            vertex(x+a, y+r/2.0)
            vertex(x, y+r)
            vertex(x-a, y+r/2.0)
            vertex(x-a, y-r/2.0)
            endShape()

    # dark borders ......................................
    stroke(dark_color)
    strokeWeight(3.0)
    strokeCap(ROUND)
    for edge in chosen_edges:
        p1, p2 = edge
        line(p1[0], p1[1], p2[0],p2[1])
    chosen_edges = find_new_edges(chosen_edges, edge_map)
    edge_map = find_edge_map(chosen_edges)

    # saving ............................................
    if save == True:
        project = "hexagons"
        output_dir = "../outputs/PNG_temps/"
        output_filename = os.path.join(
            output_dir, '{}_####.png'.format(project))
        saveFrame(output_filename)
