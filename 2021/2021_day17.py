"""
target area: x=137..171, y=-98..-73
trying to land our prob in the area after step i
initial position is [0,0]
trying to identify highest point
want to find initial velocity
min_x, max_x gives delta_t
euler_sum(n) = n*(n+1)/2
[v_x, v_y]
if v_x > 0:
    v_x -= 1
elif v_x < 0:
    v_x += 1
else:
    v_x = 0
v_y -= 1
"""


def euler_distance(n):
    return n*(n+1)/2

# vel_y_max = 97 (b/c Euler distance, would connect on -98)


def update_x_vel(x_vel):
    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1
    else:
        x_vel = 0
    return x_vel


def update_y_vel(y_val):
    y_val -= 1
    return y_val


def read_in_file(in_file):
    coordinate_list = []
    with open(in_file, 'r') as f:
        for line in f.readlines():
            coordinate_list += [coord for coord in line.rstrip().split()]
    return coordinate_list


def hit_miss(input_velocities):
    print(input_velocities)
    target_min_x, target_min_y = 137, -73
    target_max_x, target_max_y = 171, -98
    delta_t = 0
    x_pos, y_pos = 0, 0
    x_vel, y_vel = int(input_velocities.split(',')[0]), int(input_velocities.split(',')[1])
    while x_pos < target_min_x or y_pos > target_min_y:
        # print(x_pos, y_pos, x_vel, y_vel)
        x_pos += x_vel
        y_pos += y_vel
        x_vel = update_x_vel(x_vel)
        y_vel = update_y_vel(y_vel)
        if y_pos < target_max_y or x_pos > target_max_x:
            print('overshot')
            return 0, []
    if target_min_x <= x_pos <= target_max_x and target_min_y >= y_pos >= target_max_y:
        print("HIT")
        return 1, input_velocities
    else:
        print("MISS")
        return 0, []


hits = 0
hit_list = []
for i in range(172):
    for j in range(-100,100):
        hit_miss_result = hit_miss(f"{i},{j}")
        hits += hit_miss_result[0]
        hit_list += hit_miss_result[1]
print(hits)

hits = 0
for inp in read_in_file('2021_day17_input.txt'):
    hits += hit_miss(inp)
print(hits)





