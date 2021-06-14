import itertools
import time

class TrafficLight:
    __color = [['red', 7], ['yellow', 2], ['green', 7], ['yellow', 2]]
    def running (self):
        for cycle in itertools.cycle(self.__color):
            print(cycle[0])
            time.sleep(cycle[1])

traffic_light = TrafficLight()
traffic_light.running()