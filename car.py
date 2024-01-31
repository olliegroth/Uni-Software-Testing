class Car:

    def __init__(self, make, model, numPlate, doors, wheels, engineSize, currentSpeed, maxSpeed, fuelLevel):
        if len(numPlate) > 10:
            raise Exception("Number plate length cannot exceed 10")
        elif doors < 0:
            raise Exception("Minimum amount of doors is 0")
        elif wheels < 3:
            raise Exception("Minimum amount of wheels is 3")
        elif currentSpeed > maxSpeed:
            raise Exception("Current speed cannot be more than Max speed")
        elif fuelLevel > 100:
            raise Exception("Fuel level (%) cannot exceed 100")
        self.make = make
        self.model = model
        self.numPlate = numPlate
        self.doors = doors
        self.wheels = wheels
        self.engineSize = engineSize
        self.currentSpeed = currentSpeed
        self.maxSpeed = maxSpeed
        self.fuelLevel = fuelLevel

    def __repr__(self):
        return f'{self.make} {self.model} ({self.numPlate})'

    def accelerate(self, increase):
        if self.fuelLevel == 0:
            # EXCEPTION HERE
            print("The car has run out of fuel, acceleration not possible")
            return False

        if increase <= 0:
            return False

        if self.currentSpeed + abs(increase) >= self.maxSpeed:
            self.currentSpeed = self.maxSpeed
        else:
            self.currentSpeed += abs(increase)

        if self.fuelLevel - abs(increase)*0.1 >= 0:
            self.fuelLevel -= abs(increase)*0.1
        else:
            diff = -(self.fuelLevel - abs(increase)*0.1)
            self.currentSpeed = self.currentSpeed - diff*10
            self.fuelLevel = 0

    def brake(self, decrease):
        if decrease <= 0 or decrease > self.maxSpeed:
            return False

        if self.currentSpeed - abs(decrease) <= 0:
            self.currentSpeed = 0
        else:
            self.currentSpeed -= abs(decrease)

    def refuel(self, fuelIncrease):
        if fuelIncrease <= 0 or fuelIncrease > 100:
            return False

        if self.fuelLevel + abs(fuelIncrease) >= 100:
            self.fuelLevel = 100
        else:
            self.fuelLevel += abs(fuelIncrease)
