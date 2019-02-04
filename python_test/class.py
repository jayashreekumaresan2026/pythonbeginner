

class circle():
    def __init__(self ,radius):
        self.radius =radius
    def area(self):
        return 3.14*(self.radius**2)
    def perimeter(self):
        return 2* 3.15* self.radius


r= int(input("Enter radius of circle: "))
obj = circle(r)
print("Area of circle:", round(obj.area(), 5))
print("Perimeter of circle:", round(obj.perimeter(), 5))