class vehicle:
    def __init__(self, Name, MaxSpeed, Milage):
        self.Name = Name
        self.MaxSpeed = MaxSpeed
        self.Milage = Milage

class bus(vehicle):
    pass

SchoolVolvo = bus('School Volvo', 270, 1000)

print("The Name is: ", SchoolVolvo.Name,". My Max is: ",SchoolVolvo.MaxSpeed,". My Milage is: ", SchoolVolvo.Milage,sep='')