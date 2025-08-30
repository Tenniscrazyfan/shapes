
class House:
    def __init__(self, a, b, c ,d):
        self.bedroom = a
        self.bathroom = b
        self.garden = c
        self.floor = d

        print("Making an instance(making a copy of a house class)")

    def display(self):
        print("number of bedrooms = "+ self.bedroom)
        print("number of bathrooms = " + self.bathroom)
        print("garden = "+ self.garden)
        print("number of floors = "+ self.floor)
    
    def change(self):
        bedrooms = input("How many bedrooms do you want?")
        self.bedroom = bedrooms
        bathrooms = input("How many bathrooms do you want?")
        self.bathroom = bathrooms
        gardens= input("Do you want a garden?")
        self.garden = gardens
        floors = input("How many floors do you want?")
        self.floor = floors

house1 = House("2","1","no","2")
house1.display()
house1.change()
house1.display()

