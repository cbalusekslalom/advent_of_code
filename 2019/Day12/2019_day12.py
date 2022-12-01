"""
Build a space object with position & velocity
"""


class Planetary_Object():
    def __init__(self, name, x_pos, y_pos, z_pos):
        self.name = name
        self.x_position = x_pos
        self.y_position = y_pos
        self.z_position = z_pos
        self.x_velocity = 0
        self.y_velocity = 0
        self.z_velocity = 0
        self.potential = abs(self.x_position) + abs(self.y_position) + abs(self.z_position)
        self.kinetic = abs(self.x_velocity) + abs(self.y_velocity) + abs(self.z_velocity)

    def update_velocity(self, moon: 'Planetary_Object'):
        if self.x_position < moon.x_postition:
            self.x_velocity += 1
        elif self.x_position > moon.x_postition:
            self.x_velocity -= 1
        else:
            self.x_velocity += 0

        if self.y_postition < moon.y_postition:
            self.y_velocity += 1
        elif self.y_postition > moon.y_postition:
            self.y_velocity -= 1
        else:
            self.y_velocity += 0

        if self.z_postition < moon.z_postition:
            self.z_velocity += 1
        elif self.z_postition > moon.z_postition:
            self.z_velocity -= 1
        else:
            self.z_velocity += 0

    def update_postition(self):
        self.x_position += self.x_velocity
        self.y_position += self.y_velocity
        self.z_position += self.z_velocity

    def get_potential(self):
        self.potential = abs(self.x_position) + abs(self.y_position) + abs(self.z_position)
        return self.potential

    def get_kinetic(self):
        self.kinetic = abs(self.x_velocity) + abs(self.y_velocity) + abs(self.z_velocity)
        return self.kinetic

    def get_position(self):
        return [self.x_position, self.y_position, self.z_position]

    def get_velocity(self):
        return [self.x_velocity, self.y_velocity, self.z_velocity]

"""
<x=6, y=-2, z=-7>
<x=-6, y=-7, z=-4>
<x=-9, y=11, z=0>
<x=-3, y=-4, z=6>
"""
moon1 = planetary_object('a', 6, -2, -7)
moon2 = planetary_object('b', -6, -7, -4)
moon3 = planetary_object('c', -9, 11, 0)
moon4 = planetary_object('d', -3, -4, 6)

moon_list = [moon1, moon2, moon3, moon4]

for i in moon_list:
    for j in moon_list:
        if i != j:
            i.update_velocity(j)
    print(i.name, i.get_velocity())

for i in moon_list:
    i.update_postition()

for i in moon_list:
    print(f"{i.name} \t {i.get_position()} \t {i.get_velocity()} \t {i.get_potential()} \t {i.get_kinetic()}")
