with open('input.txt') as f:
    tupleList = []
    for line in f.readlines():
        tupleList.append(tuple([int(x) for x in line.split(',')]))

def tuple_diff(tup1:tuple, tup2:tuple) -> tuple:
    if len(tup1) != len(tup2):
        return "Invalid lengths"
    return tuple([tup1[i] + tup2[i] for i in range(len(tup1))])


x_val = [1, -1, 0, 0, 0, 0]
y_val = [0, 0, 1, -1, 0, 0]
z_val = [0, 0, 0, 0, 1, -1]
faces_shown = 0
empty_coords = []
for tup in tupleList:
    cube_faces = 6
    for adjacent in list(zip(x_val,y_val,z_val)):
        adj_cube = tuple_diff(tup, adjacent)
        if adj_cube in tupleList:
            cube_faces -= 1
        elif adj_cube not in tupleList:
            empty_coords.append(adj_cube)
    faces_shown += cube_faces
print(faces_shown)

