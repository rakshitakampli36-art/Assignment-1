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
    def __init__(self,mileage,cost,tyers,hp):
        super().__init__(mileage,cost)
        self.tyers=tyers
        self.hp=hp
    def show_car_detailes(self):
        print("I am a car")
        print("Number of tyers are ",self.tyers)
        print("Value of horse power is ",self.hp)
c2=car(20,12000,4,300)
c2.show_car_detailes()
