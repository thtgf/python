class Automobile:
    name= "name"
    yearofrelease = "0000"
    manufacturer ="BMW"
    enginepower ="enginepower"
    color = "color"
    price = "price"

    def print_info(self):
        print("Данные автомобиля".center(40 ,"*"))
        print(f"Название модели: {self.name}\nГод выпуска:{self.yearofrelease}\nПроизводитель:{self.manufacturer}\nМощность двигателя:{self.enginepower}\nЦвет машины:{self.color}\nЦена:{self.price}")
        print("=" * 40)
    def input_info(self,first_name,yearofrelease,manufacturer,enginepower,color,price):
        self.name = first_name
        self.yearofrelease = yearofrelease
        self.manufacturer = manufacturer
        self.enginepower = enginepower
        self.color = color
        self.price = price
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_yearofrelease(self,name):
        self.yearofrelease= name
    def get_yearofrelease(self):
        return self.yearofrelease
    def set_manufacturer(self,name):
        self.manufacturer= name
    def get_manufacturer(self):
        return self.manufacturer
    def set_enginepower(self,name):
        self.enginepower =name
    def get_enginepower(self):
        return self.enginepower
    def set_color(self,name):
        self.color = name
    def get_color(self):
        return self.color
    def set_price(self,name):
        self.price = name
    def get_price(self):
        return self.price

h1 = Automobile()
h1.print_info()
h1.input_info("x7 m50i","2021","BMW","530 л.с.","white","10790000")
h1.print_info()
h1.set_name("x7 m50i ")
print(h1.get_name())
h1.set_yearofrelease("2021")
print(h1.get_yearofrelease())
h1.set_manufacturer("BMW")
print(h1.get_manufacturer())
h1.set_enginepower("530 л.с.")
print(h1.get_enginepower())
h1.set_color("white")
print(h1.get_color())
h1.set_price("10790000")
print(h1.get_price())