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

#mission 4
class Athleth:
    def __init__(self,name,country):
        self.name=name
        self.country=country
    def greet(self):
        print(f"{self.name} represent {self.country}")
class Swimmer(Athleth):
    def __init__(self, name, country,stroke_style):
        super().__init__(name, country)
        self.stroke_style=stroke_style
class Runner(Athleth):
    def __init__(self, name, country,best_distance):
        super().__init__(name, country)
        self.best_distance=best_distance
class Cyclist(Athleth):
    def __init__(self, name, country,race_type):
        super().__init__(name, country)
        self.race_type=race_type
lior=Swimmer("lior","israel","freestyle")
avi=Runner("avi","kenya","maratohn")
jan=Cyclist("jan","france","road")
lior.greet()
avi.greet()
jan.greet()

#mission 5
class Athleth:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def warm_up(self):
        print(f"{self.name} is warming up")
class Gymnast(Athleth):
    def __init__(self, name, age,apparatus):
        super().__init__(name, age)
        self.apparatus=apparatus
    def compete(self):
        print(f"{self.name} competes on the {self.apparatus}")
class Swimmer(Athleth):
    def __init__(self, name, age,stroke):
        super().__init__(name, age)
        self.storke=stroke
    def compete(self):
        print(f"{self.name} competes in {self.storke}")
ana=Gymnast("ana",19,"rings")
ana.warm_up()
ana.compete()
ben=Swimmer("ben",12,"butterfly")
ben.warm_up()
ben.compete()

#mission 6
class Athleth:
    def __init__(self,name,age,years_active):
        self.name=name
        self.age=age
        self.years_active=years_active
    def experince(self):
        print(f"{self.name} has been active for {self.years_active} years")
class Teamsportplayer(Athleth):
    def __init__(self, name, age, years_active,team_name):
        super().__init__(name, age, years_active)
        self.team_name=team_name
    def team_info(self):
        print(f"{self.name} plays for {self.team_name}")
gal=Teamsportplayer("gal",28,10,"real madrid")
gal.experince()
gal.team_info()

#mission 7
class Athleth:
    def __init__(self,name,sport):
        self.name=name
        self.sport=sport
        self.personal_best=None
    def set_record(self,value):
        self.personal_best=value
        print("update succsefully")
    def has_record(self):
        return self.personal_best!=None
class sprinter(Athleth):
    def __init__(self, name,):
        super().__init__(name, "100m sprint")
usain=sprinter("usain")
print(usain.has_record())
usain.set_record(12.5)
print(usain.has_record())
print(usain.personal_best)
        
#mission 8
class Athleth:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.sessions_completed=0
    def train(self):
        self.sessions_completed+=1
    def sessions_neened(self,target):
        if target-self.sessions_completed>0:
            return target-self.sessions_completed
        else:
            return 0
class Triathlete(Athleth):
    def __init__(self, name, age,discipline):
        super().__init__(name, age)
        self.discipline=discipline
    def describe(self):
        print(f"Triathlete {self.name}, age {self.age}, discipline:{self.discipline}")
dan=Triathlete("dan",26,"cycling")
dan.train()
dan.train()
dan.train()
dan.train()
dan.train()
print(dan.sessions_neened(10))
dan.describe()

#mission 9
class Athleth:
    def __init__(self,name,age,position):
        self.name=name
        self.age=age
        self.position=position
    def player_card(self):
        print(f"name; {self.name}, age:{self.age}, position:{self.position}")
class Basketballplayer(Athleth):
    def __init__(self, name, age, position,jersey_number):
        super().__init__(name, age, position)
        self.jersey_number=jersey_number
    def full_profile(self):
        self.player_card()
        print(f"jersey: #{self.jersey_number}")
chaim=Basketballplayer("cahim",22,"center",11)
yossi=Basketballplayer("yossi",24,"shooting",19)
lebron=Basketballplayer("lebron",35,"pg",77)
chaim.full_profile()
yossi.full_profile()
lebron.full_profile()

#mission 10
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"hi i am {self.name}")

class Athleth(person):
    def __init__(self, name, age,sport):
        super().__init__(name, age)
        self.sport=sport
    def train(self):
        print(f"{self.name} is training for {self.sport}")
class ProfssionalAthleth(Athleth):
    def __init__(self, name, age, sport,sponsor):
        super().__init__(name, age, sport)
        self.sponsor=sponsor
    def sponsor_info(self):
        print(f"{self.name} is sponsored by {self.sponsor}")
cr7=ProfssionalAthleth("ronaldo",41,"fotball","adidas")
cr7.greet()
cr7.train()
cr7.sponsor_info()