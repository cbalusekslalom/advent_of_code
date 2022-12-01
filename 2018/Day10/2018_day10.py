from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button
import re


def read_file(in_file):
    posvel_list = []
    pos_list = []
    vel_list = []
    with open(in_file,'r') as f:
        for line in f.readlines():
            posvel_list.append([i for i in re.split(r"position=<(.*)> velocity=<(.*)>", line.rstrip()) if i != ''])
    for inp in posvel_list:
        pos_list.append([int(j.strip()) for j in inp[0].split(', ')])
        vel_list.append([int(k.strip()) for k in inp[1].split(', ')])
    return pos_list, vel_list


class aligning_stars():
    def __init__(self, pos, vel):
        pos = [int(i) for i in pos.split(',')]
        vel = [int(j) for j in vel.split('')]
        self.position_x = pos[0]
        self.position_y = pos[1]
        self.velocity_x = vel[0]
        self.velocity_y = vel[1]
        self.initial_time = 0

    def update_position(self,time):
        delta_time = time - self.initial_time
        self.position_x = self.position_x + delta_time * self.velocity_x
        self.position_y = self.position_y + delta_time * self.velocity_y
        self.initial_time = time



pos_list, vel_list = read_file('2018_day10_input.txt')

dt = 10

particles = np.zeros((len(pos_list),2),dtype=[("position", int), ("velocity", int)])
particles["position"] = np.column_stack([pos_list])
particles["velocity"] = np.column_stack([vel_list])
particles["position"] = particles["position"] + particles["velocity"]*dt
xs, ys = zip(*particles["position"])
xmin, xmax = min(xs)-10, max(xs)+10
ymin, ymax = min(ys)-10, max(ys)+10
fig, ax = plt.subplots()
ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
scatter = ax.scatter(particles["position"][:,0], particles["position"][:,1])

def update(frame_number):
    xs, ys = zip(*particles["position"])
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    ax.set_xlim(xmin-20, xmax+20)
    ax.set_ylim(ymin-20, ymax+20)
    particles["position"] = particles["position"] + particles["velocity"]*dt
    scatter.set_offsets(particles["position"])
    return scatter,

anim = FuncAnimation(fig, update, frames=(0, 1200), interval=10)
plt.show()


