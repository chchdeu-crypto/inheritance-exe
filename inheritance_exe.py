#mission 1
class Athleth:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athleth")
class Swimmer(Athleth):
    def __init__(self, name, age):
        super().__init__(name, age)
tom=Swimmer("tom",22)
tom.introduce()

#mission 2
class Athleth:
    def __init__(self,name,age,sport):
        self.name=name
        self.age=age
        self.sport=sport
    def describe(self):
        print(f"{self.name} competes in {self.sport}")
class Runner(Athleth):
    def __init__(self, name, age):
        super().__init__(name, age, "running")
sara=Runner("sara",25)
sara.describe()