class Person:
    def __init__(self,person__name,person__old):
        self.__person__name ='Irina'
        self.__person__old = 26
    def __set_person__name(self,person__name):
        self.__person__name ='Igor'
    def __set_person__old(self,person__old):
        self.__person__old = 31
    def __get_person__name(self,person__name):
        return self.__person__name
    def __get_person__old(self,person__old):
        return self.__person__old
    def __delete_person__name(self,person__name):
        del self.__person__name
    person__old = property(__get_person__old,__set_person__old)
    person__name = property(__get_person__name,__set_person__name,__delete_person__name)



p1 = Person('Irina',26)

print(p1.__dict__)
p1.person__name ='Igor'
p1.person__old = '31'
print(p1.person__name)
print(p1.person__old)
