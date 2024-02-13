from unitTesting.car import Car

def test_car_creation():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 0, 102, 100)
    assert firstCar.make == "Skoda"
    assert firstCar.model == "Fabia"
    assert firstCar.numPlate == "GR07 THO"
    assert firstCar.doors == 5
    assert firstCar.wheels == 4
    assert firstCar.engineSize == 1.2
    assert firstCar.currentSpeed == 0
    assert firstCar.maxSpeed == 102
    assert firstCar.fuelLevel == 100