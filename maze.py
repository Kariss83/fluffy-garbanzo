#!/usr/bin/env python3
# coding: utf-8

class Position:

    def __init__(self, longitude, latitude):
        self.longi = longitude
        self.latit = latitude


class Maze:

    NUMBER_OF_LINES = 16
    ZONES = []
    
    def __init__(self,corner1, corner2):
        self.corner1 = corner1
        self.corne2 = corner2
    
    @classmethod
    def initialize_zones(cls):
        for latitude in range(1, cls.NUMBER_OF_LINES, 1):
            for longitude in range(1, cls.NUMBER_OF_LINES, 1):
                    bottom_left_corner = Position(longitude, latitude)
                    top_right_corner = Position(longitude + 1, latitude + 1)
                    zone = Maze(bottom_left_corner, top_right_corner)
                    cls.ZONES.append(zone)
        print(len(cls.ZONES))

def main():
    Maze.initialize_zones()
        
if __name__ == "__main__":
    main()
