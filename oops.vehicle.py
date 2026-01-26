class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_detailes(self):
       print("I am Vehicle")
       print("Mileage of Vehicle is :",self.mileage)
       print("Cost of Vehicle is :",self.cost)
v1=Vehicle(500,500)
v1.show_detailes()
class car(Vehicle):
    def show_car(self):
        print("I am a car")
c1=car(200,1200)
c1.show_detailes()
c1.show_car()









