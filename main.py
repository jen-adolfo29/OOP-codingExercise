class ClubMembers:
    def __init__(self, name, bday, age, fav_food, goal):
        self.name = name
        self.bday = bday
        self.age = age
        self.fav_food = fav_food
        self.goal = goal

    def display(self):
        print("Name:", self.name)
        print("Birthday:", self.bday)
        print("Age:", self.age)
        print("Favorite Food:", self.fav_food)
        print("Goal:", self.goal)

class ClubOfficers(ClubMembers):
    def __init__(self, name, bday, age, fav_food, goal, position):
        super().__init__(name, bday, age, fav_food, goal)
        self.position = position

    def display2(self):
        print()
        print("Name:", self.name)
        print("Birthday:", self.bday)
        print("Age:", self.age)
        print("Favorite Food:", self.fav_food)
        print("Goal:", self.goal)
        print("Position:", self.position)

m_1 = ClubMembers("Jen", "November 29", "23", "Adobong Manok", "To be happy")
o_4 = ClubOfficers("Vivi", "February 6", "20", "Meat", "Travel", "Captain")

m_1.display()
o_4.display2()