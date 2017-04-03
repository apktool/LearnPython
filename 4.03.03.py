# 工厂模式
class Shape(object):
    def __init__(self):
        pass

    def draw(self):
        pass

    def erase(self):
        pass


class Circle(Shape):
    def __init__(self, radius=0):
        self.__radius = radius

    def draw(self):
        print('draw circles')

    def erase(self):
        print('erase circles')

    def get_radius(self):
        print('circle\'s radius is %d' % self.__radius)


class Rectangle(Shape):
    def __init__(self, width=3, high=4):
        self.__width = width
        self.__high = high

    def draw(self):
        print('draw circles')

    def erase(self):
        print('erase circles')

    def get_area(self):
        print('rectangle\'s area is %d' % (self.__width * self.__high))


class ShapeFactory(object):
    def factory(self, which):
        if which == 'Circle':
            app = Circle()
        elif which == 'Rectangle':
            app = Rectangle()
        else:
            app = None
        return app


if __name__ == '__main__':
    fact = ShapeFactory()
    shape = fact.factory('Circle')
    shape.draw()

    fact = ShapeFactory()
    shape = fact.factory('Rectangle')
    shape.get_area()
