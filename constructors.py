class Point:
    def __init__(self,x,y):         # constructor function
        self.x=x                    # dunder method which is automatically called
        self.y=y


    def move(self):
        print("Move around")        # inside a class there will be func(methods) and attributes
                                                

    def draw(self):
        print("Draw somthing")
    

point1=Point(10,20)                 # calling the constructor function
# print(point1.x)
print(point1.x)
print(point1.y)