from unitTestingPractise.car import Car

def test_accelerate_currentSpeed():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 0, 102, 100)
    firstCar.accelerate(50)
    assert firstCar.currentSpeed == 50

def test_accelerate_fuelLevel():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 0, 102, 100)
    firstCar.accelerate(50)
    assert firstCar.fuelLevel == 95