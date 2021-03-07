# ********************************************************************
# HOLLOW HEXAGON -- variations
# rOsita fu
# 2021-03-07
# github.com/atisor73
# ********************************************************************

save = True
loop = True
frame_rate = 2
# ************************ CONSTANTS ***********************
width, height = 1200, 700
paddingx, paddingy = 100, 100

r = 15

bg_color = "#000208"
# dark_color =  "#777D90"
dark_color = "#D7D2BE"
n_edges = 125                      # background lines
n_clusters = 50                    # num of initial seeds
cluster_min, cluster_max = 5, 10   # random interval of neighbors
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
            elif (x1 > 2*a*(n_cols-1)) or (x2 > 2*a*(n_cols-1)):
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

# ******************** BUILDING GRID *********************
a = r*cos(PI/6.0)
n_rows = int((height-2.0*paddingy)/(1.5*r))
n_cols = int((width-2.0*paddingx)/(2.0*a))

center_xs, center_ys = [], []
for i in range(n_rows):
    if i % 2 == 1: center_xs.append([2*j*a for j in range(n_cols)])
    else: center_xs.append([(1+(2*j))*a for j in range(n_cols-1)])
    center_ys.append([ (3*i + 2)/2.0*r for _ in range(n_cols)])

# ******************** CHOOSING EDGES *********************
edges = []
for xrow, yrow in zip(center_xs, center_ys):
    for x, y in zip(xrow, yrow):
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

# ****************** CHOOSING CLUSTERS *******************
seed_i = [int(random(len(edges))) for _ in range(n_clusters)]
for i in seed_i:
    neighbors1 = [edges[(i+j)%len(edges)] for j in range(0,
                                            int(random(cluster_min, cluster_max)))]
    neighbors2 = [edges[(i+j+int(len(edges)/n_rows))%len(edges)]
                            for j in range(0, int(random(cluster_min, cluster_max)))]
    chosen_edges.extend(neighbors1)
    chosen_edges.extend(neighbors2)

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
