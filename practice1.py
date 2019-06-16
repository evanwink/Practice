class House():

    # Class variables
    roof = True
    variable = [1,2,3,4]

    # Initialize instance with attributes
    def __init__(self, color, size):
        self.color = color
        self.size = size

    # method
    def july4(self):
        print(f"Yay fireworks! My house is {self.color}.")
        return None




h = House("blue", 1000)
h2 = House("red", 500)

h.july4()
h2.july4()


