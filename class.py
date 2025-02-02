class Point:
    def move(self):
        print("Move around")        # inside a class there will be func(methods) and attributes
                                                

    def draw(self):
        print("Draw somthing")
    

point1=Point()      # creating an object of class Point
point1.draw()
point1.move()
# print(point1.x)
point1.x=10                          # assinging attributes not present in the class Point
point1.y=20
print(point1.x)
print(point1.y)

point2=Point()
point2.draw()
# print(point2.x)
point2.x=125
point2.y=250
print(point2.x)
print(point2.y)