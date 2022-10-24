import random


class Programmer:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 0
        self.academic_performance = 0
        self.alive = True

    def to_progarmming(self):
        print("Time for working!")
        self.progress += 0.5
        self.gladness -= 3
        self.money += 600
        self.academic_performance = 0.4

    def to_sleep(self):
        print("I will to sleep")
        self.gladness += 5

    def to_chill(self):
        print("Time relax")
        self.gladness += 4
        self.progress -= 0.2
        self.money -= 300
        self.academic_performance -= 0.3

    def is_alive(self):
        if self.progress < -0.1:
            print("You fired")
            self.alive = False
        elif self.gladness <= 1:
            print("Depression")
            self.alive = False
        elif self.progress >= 8:
            print("Overload")
            self.alive = False
        elif self.money <= 0:
            print("Enough money")
            self.alive = True
        elif self.academic_performance < 0.1:
            print("bad academic performance")
            self.alive = True
        elif self.academic_performance > 9:
            print("high academic performance")
            self.alive = True

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def life(self, day):
        day = " Day " + str(day) + " of " + "life " + self.name
        print(f"{day:=^50}")
        life_cube = random.randint(1, 3)
        if life_cube == 1:
            self.to_progarmming()
        elif life_cube == 2:
            self.to_sleep()
        elif life_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Programmer("Dmitriy ")

for day in range(365):
    if nick.alive == False:
        break
    nick.life(day)