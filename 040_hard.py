import random
import math

def random_point():
    return (random.random(), random.random())

def distance((ax, ay), (bx, by)):
    xdist = ax - bx
    ydist = ay - by
    return math.sqrt(math.pow(xdist, 2) + math.pow(ydist, 2))

def min_distance_generator(new_point):
    yield new_point
    while True:
        

def generate_array(size):
    return [random_point() for p in range(size)]


