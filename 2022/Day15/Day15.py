
def openFile(inFile):
    sensor_List = []
    beacon_List = []
    with open(inFile) as f:
        for line in f.readlines():
            input = line.split(' ')
            sensor_List.append((int(input[2].strip()[2:-1]), int(input[3].strip()[2:-1])))
            beacon_List.append((int(input[8].strip()[2:-1]), int(input[9].strip()[2:])))
    return sensor_List, beacon_List


class Sensor:

    def __init__(self, coord, beacon):
        self.position = coord
        self.closest_beacon = beacon
        self.distance = abs(self.closest_beacon[0] - self.position[0]) + abs(self.closest_beacon[1] - self.position[1])
        self.perimeter = []

    def make_perimeter(self):
        for i in range(-1*self.distance, self.distance + 1):
            for j in [-1*self.distance + abs(i), self.distance - abs(i)]:
                self.perimeter.append((i, j))

    def get_extended_perimeter(self, dist):
        self.extendedPerimeter = []
        for i in range(-1*self.distance - abs(dist), self.distance + 1 +abs(dist)):
            for j in [-1*self.distance + abs(i) - abs(dist), self.distance - abs(i) + abs(dist)]:
                self.extendedPerimeter.append((i, j))




def manhattan_distance(tup, val) -> list:
    ## same as the BHS method in day 10/11?
    ## For a sensor location, need to calculate the distance of each tuple in any direction
    ## once we reach the destination, then we capture all tuples less than said distance
    ## Get Manhattan distance b/w sensor & beacon
    ## Collect all Tuples in that distance
    sensor, beacon = tup[0], tup[1]
    inList = []
    y_dist = abs(val - sensor[1])
    distance = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])

    for i in range(-distance + y_dist, distance - y_dist + 1):
            inList.append(sensor[0]+i)
    return inList


def main_pt1():
    inVal = 2000000
    sensorList = []
    sensors_list, beacon_list = openFile('input.txt')
    sensorList.extend(manhattan_distance(inp, inVal) for inp in list(zip(sensors_list, beacon_list)))
    sb_counter = 0
    for inp in set(beacon_list):
        if inp[1] == inVal:
            sb_counter += 1
    actualList = [x for l in sensorList for x in l]
    print(set(actualList))
    print(len(set(actualList)) - sb_counter)
    print(max(actualList) - min(actualList))


def main_pt2():
    sensors_list, beacon_list = openFile('input.txt')
    key = 0
    sensor_dict = {}
    for tup in list(zip(sensors_list, beacon_list)):
        sensor_dict[key] = Sensor(tup[0], tup[1])
        key += 1



if __name__ == '__main__':
    main()
