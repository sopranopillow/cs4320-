#!/usr/bin/python
import os, sys, re

def process_args(argv):
    argv = argv[1:]

    if '-A':
        algorithm = 'a*'
    elif '-I':
        algorithm = 'iter'
    elif '-B':
        algorithm = 'bfs'
    else:
        algorithm = None

    path = argv[argv.index('-p') + 1]
    return algorithm, path

def get_data(path):
    f = open(path, 'r')
    clean = lambda x: [int(i.strip('\n')) for i in x] # using this to remove next line escape char and convert to int
    dimensions = clean(f.readline().split(' '))
    start_location = clean(f.readline().split(' '))
    goal_location = clean(f.readline().split(' '))
    map = []

    for i in range(dimensions[0]):
        map.append(clean(f.readline().split(' ')))

    return dimensions, start_location, goal_location, map

if __name__ == "__main__":
    algorithm, path = process_args(sys.argv)
    dimensions, start_location, goal_location, map = get_data(path)