
class Car:
    brand_name = "Lamborghini"   # Class variable shared by all cars
    
    def __init__(self):
        self.speed = 0
        self.gear_no = 0
        self.engine_on = False

    def engineStart(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"{Car.brand_name} engine started.")
        else:
            print("Engine is already on.")
    
    def engineStop(self):
        if self.engine_on:
            self.engine_on = False
            self.speed = 0
            self.gear_no = 0
            print(f"{Car.brand_name} engine stopped.")
        else:
            print("Engine is already off.")

    def accelerate(self):
        if not self.engine_on:
            print("Start the engine first!")
            return
        if self.speed < 300:
            self.speed += 25
            print(f"Accelerating... Speed: {self.speed} kmph")
        else:
            print("Max speed reached (300 kmph)!")

    def brake(self):
        if self.speed > 0:
            self.speed -= 25
            if self.speed < 0:
                self.speed = 0
            print(f"Braking... Speed: {self.speed} kmph")
        else:
            print("Car is already stationary.")

    def sudden_brake(self):
        self.speed = 0
        print("Sudden brake applied! Speed is now 0 kmph.")

    def gear(self):
        if self.gear_no < 5:
            self.gear_no += 1
            print(f"Gear changed to {self.gear_no}")
        else:
            print("Already in top gear (5).")


# Example usage:
car1 = Car()
car1.engineStart()
car1.gear()
car1.accelerate()
car1.accelerate()
car1.brake()
car1.gear()
car1.accelerate()
car1.sudden_brake()
car1.engineStop()
