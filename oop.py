class phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
         print(self.color)
    def show_cost(self):
        print(self.cost)
    def make_call(self):
        print("Making phone call")
    def Play_game(self):
        print("Playing Games")
p1=phone()
p1.set_color('red')
p1.set_cost(25000)
p1.show_color()
p1.show_cost()
p1.make_call()
p1.Play_game()
