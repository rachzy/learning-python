from time import sleep


class Car:
    def __init__(self, brand, year, license):
        self.brand = brand
        self.year = year
        self.license = license
        self.turnedOn = False
        self.acOn = False
        self.headlightOn = False
        pass
    
    def turnOn(self):
        if(self.turnedOn):
            return print("The car is already turned on.")

        print("Turning the car on...")
        sleep(2)

        self.turnedOn = True
        print("The car is ready to move on!")
        return self
    
    def turnACOn(self):
        if(self.acOn):
            return print("The car's AC is already turned on.")

        print("Turning the AC on...")
        sleep(0.5)

        self.turnedOn = True
        print("AC is now turned on!")
        return self
    
    def turnHeadlightsOn(self):
        if(self.headlightOn):
            return print("The car's headlights are already on.")
        
        print("Turning the headlights on...")
        sleep(1)

        self.turnedOn = True
        print("Lights up! The headlights are on!")
        return self


Ferrari = Car("Ferrari Portofino", 2012, "USA07041")

Ferrari.turnOn().turnACOn().turnHeadlightsOn()