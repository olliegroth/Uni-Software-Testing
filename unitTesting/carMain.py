from car import Car

firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 0, 102, 100)
secondCar = Car("Porsche", "944", "OG23 SEP", 5, 4, 2.5, 0, 140, 100)

listOfCars = [firstCar, secondCar]

print("\nFirst Car: " f'{ firstCar.make, firstCar.model, firstCar.numPlate, firstCar.doors, firstCar.wheels, firstCar.engineSize, firstCar.currentSpeed,firstCar.maxSpeed, firstCar.fuelLevel}')
print("\nSecond Car: " f'{ secondCar.make, secondCar.model, secondCar.numPlate, secondCar.doors, secondCar.wheels, secondCar.engineSize, secondCar.currentSpeed,secondCar.maxSpeed, secondCar.fuelLevel}')

print(listOfCars)
carSelection = int(input("What unitTesting would you like to select? [1] or [2]: "))