#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
import math

class Graph:
    def __init__(self, dimensions):  # assuming all are weighted and directed
        self.edges = {}
        self.dimensions = dimensions

    def __str__(self):
        return str(self.edges)

    def __len__(self):
        return self.dimensions[0] * self.dimensions[1]

    def draw_graph(self):
        fig, ax = plt.subplots()
        n = len(self)
        r = 30
        coords = {}

        # set coordinates coords = [[x, y]]
        for r in range(self.dimensions[0]):
            for c in range(self.dimensions[1]):
                coords[str(r) + ', ' + str(c)] = [.2*c, -.2*r]

        # draw edges
        for r in range(self.dimensions[0]):
            for c in range(self.dimensions[1]):
                coordinate = str(r) + ', ' + str(c)
                if self.edges.get(coordinate):
                    for e in self.edges[coordinate]:
                        src = coords[coordinate]
                        dest = coords[str(e[0][0]) + ', ' + str(e[0][1])]
                        ax.plot([src[0], dest[0]],[src[1], dest[1]],linewidth=1,color="k")

        # draw nodes
        for coord in coords:
            ax.text(coords[coord][0], coords[coord][1], coord, size=10, ha="center", va="center",
                bbox=dict(facecolor='w',boxstyle=BoxStyle("Round", pad=.4)))

        # ax.set_aspect(1.0)
        ax.axis('off')

    def insert_edge(self, s_r, s_c, d_r, d_c, w): # all edges are connected from the sides
        source = str(s_r) + ', ' + str(s_c)
        if self.edges.get(source) == None:
            self.edges[source] = [[[d_r, d_c],w]]
        else:
            self.edges[source].append([[d_r, d_c],w])

    def A_s(self, g, start_goal, goal_location, dimensions):
        pass

    def iterative_deepening(self, g, start_goal, goal_location, dimensions):
        pass

    def bfs(self, g, start_goal, goal_location, dimensions):
        q = []
        visited = np.zeros(self.dimensions, dtype=bool)

        q.append(start_goal)
        visited[start_goal] = True

        while q:
            s = q.pop(0)
            print('s ' + str(s))
            if g.edges.get(str(s[0]) + ', ' + str(s[1])):
                for i in g.edges[str(s[0]) + ', ' + str(s[1])]:
                    if visited[i[0][0],i[0][1]] == False:
                        print('q ' + str(q))
                        q.append(i[0])
                        visited[i[0][0],i[0][1]] = True