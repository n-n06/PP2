class Dinosaur():
    def __init__(self, type, diet):
        self.type = type
        self.diet = diet
    def roar():
        print("Roar")
    def set_name(self, name):
        self.name = name
    def get_name(self):
        print(self.name)
t_rex = Dinosaur("T-rex", "Carnivore")
t_rex.set_name("T-Rex")
t_rex.get_name()
