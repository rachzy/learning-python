from time import sleep


class Computer:
    def __init__(self, brand: str, ram: int, gpu: int):
        self.brand = brand
        self.ram = ram
        self.gpu = gpu
        self.online = False
    
    def turnOn(self):
        if(self.online):
            return print("I'm already on!")
        
        print("Turning on...")
        sleep(3)
        self.online = True
        print("I'm on and ready!")
        return self
    
    def turnOff(self):
        if(self.online == False):
            return print("The computer is already turned off")
        
        print("Turning off...")
        sleep(3)
        self.online = True
        print("Completely ended")
        return self

    def restart(self):
        if(self.online == False):
            return print("The computer has to be turned on to be rebooted")
        self.turnOff().turnOn()
        return self

    def openConfigs(self):
        print("Opening configs...")
        sleep(2)
        print("=" * 30)
        print("BRIGHTNESS - ENHANCEMENT - PICTURES - ADVANCED")
        print("=" * 30)
        return self
    
computer1 = Computer("Asus", 8, "Nvidia")
computer2 = Computer("Dell", 12, "AMD")

computer1.turnOn().turnOn()