import math


class Point:

    def __init__(self, x, y):
        self.__coord_x = x
        self.__coord_y = y
        self.distance = None

    @property
    def coord_x(self):
        return self.__coord_x

    @coord_x.setter
    def coord_x(self, x):
        self.__coord_x = x

    @property
    def coord_y(self):
        return self.__coord_y

    @coord_y.setter
    def coord_y(self, y):
        self.__coord_y = y

    def get_coord(self):
        return self.coord_x, self.coord_y

    def set_coord(self, x, y):
        self.coord_x = x
        self.coord_y = y

    def distance_to_the_another_point(self, point_x, point_y):
        self.distance = math.sqrt((self.coord_x - point_x)**2
                                  + (self.coord_y - point_y)**2)
