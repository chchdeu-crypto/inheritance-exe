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

#mission 3
class Athleth:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athleth")   
class Cyclist(Athleth):
    def __init__(self, name, age,bike_brand):
        super().__init__(name, age)
        self.bike_brand=bike_brand
    def discribe_gear(self):
        print(f"cyclist {self.name} rides a {self.bike_brand}")
rider1=Cyclist("chaim",22,"trek")
rider1.introduce()
rider1.discribe_gear()