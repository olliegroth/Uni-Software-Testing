from car import Car

firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 0, 102, 100)
secondCar = Car("Porsche", "944", "OG23 SEP", 5, 4, 2.5, 0, 140, 100)

listOfCars = [firstCar, secondCar]

print("\nFirst Car: " f'{ firstCar.make, firstCar.model, firstCar.numPlate, firstCar.doors, firstCar.wheels, firstCar.engineSize, firstCar.currentSpeed,firstCar.maxSpeed, firstCar.fuelLevel}')
print("\nSecond Car: " f'{ secondCar.make, secondCar.model, secondCar.numPlate, secondCar.doors, secondCar.wheels, secondCar.engineSize, secondCar.currentSpeed,secondCar.maxSpeed, secondCar.fuelLevel}')

firstCar.accelerate(50)
print(f'\nAfter accelerating, the first car has a speed of {firstCar.currentSpeed}mph and a fuel level of {firstCar.fuelLevel}%')

firstCar.brake(20)
print(f'\nAfter breaking, the first car has a speed of {firstCar.currentSpeed}mph and a fuel level of {firstCar.fuelLevel}%')

firstCar.refuel(10)
print(f'\nAfter refueling, the first car has a fuel level of {firstCar.fuelLevel}%')

print(listOfCars)
carSelection = int(input("What car would you like to select? [1] or [2]: "))

