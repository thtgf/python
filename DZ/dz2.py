import math


class Area:
    count =0
    @staticmethod
    def triangle_area_1(a, b ,c):
        p = (a+b+c) /2
        Area.count +=1
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    @staticmethod
    def triangle_area_2(a,h):
        Area.count += 1
        return 0.5*a*h
    @staticmethod
    def square_area(a):
        Area.count += 1
        return a**2
    @staticmethod
    def rect_area(a,b):
        Area.count += 1
        return a*b
    @staticmethod
    def get_count():
        return Area.count
print(f"Площадь треугольника по формуле Герона:{Area.triangle_area_1(3,4,5)}")
print(f"Площадь треугольнига через основание и высоту:{Area.triangle_area_2(6,7)}")
print(f"Площадь квадрата:{Area.square_area(7)}")
print(f"Площадь прямоугольника:{Area.rect_area(2,6)}")
print(f"Количество подсчётов площади:{Area.get_count()}")