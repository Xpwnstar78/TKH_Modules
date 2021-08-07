import math
import math as mt
# from math import log, pi
# from numpy import asarray


def main():

    a = 5
    print(type(a))

    alist = [1, 2, 'a']
    print(type(alist))

    heights = [5, 4, 6, 7, 3, 5]
    heights.sort()
    print(heights)

    alist.reverse()
    print(alist)

    astring = 'hello world'
    bstring = astring.replace('world', 'there!')
    print(bstring)

    print(dir(alist))

    class Rectangle:
        def __init__(self, height, width):
            self.height = height
            self.width = width

        def area(self):
            area = self.height * self.width
            return area

    rect1 = Rectangle(12, 10)

    print(type(rect1))

    print(rect1.height)

    print(rect1.width)

    print(rect1.area())

    print(dir(rect1))

    print(type(math))

    print(dir(math))

    # print(math.log(100, 10))

    print(math.pi)

    # print(mt.log(100, 10))

    # print(log(100, 10))


if __name__ == '__main__':
    main()
