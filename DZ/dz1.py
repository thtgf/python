class Order:
    def  __init__(self,name,price,volume):
        self.name= name
        self.price= price
        self.volume= volume

o=Order("apple",5,10)
print((o))