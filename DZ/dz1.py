class Figure:
    def __init__(self,color):
        self.__color = color
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,c):
        self.__color =c

class Rectangle (Figure):
    def __init__(self,width, height,color):
        self.width = width
        self.__height = height
        super().__init__(color)
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        if value <0:
            raise ValueError(f"Значение{value}должно быть оложительным числом")
        self.__width=value
    def area(self):
        print(f"Прямоугольник {self.color}.Площадь:", end="")
        return self.__width *self.__height

rect = Rectangle (-10,20,"green")
print(rect.area())