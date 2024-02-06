from unitTestingPractise.car import Car

def test_accelerate_maxSpeed_cap():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 0, 102, 100)
    firstCar.accelerate(150)
    assert firstCar.currentSpeed == 102

def test_accelerate_fuelLevel_cap():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 50, 102, 1)
    firstCar.accelerate(20)
    assert firstCar.fuelLevel == 0

def test_accelerate_currentSpeed_adjustment():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 50, 102, 1)
    firstCar.accelerate(20)
    assert firstCar.currentSpeed == 60

def test_zero_accelerate_value():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 50, 102, 1)
    firstCar.brake(0)
    assert firstCar.currentSpeed == 50

def test_negative_accelerate_value():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 50, 102, 1)
    firstCar.brake(-20)
    assert firstCar.currentSpeed == 50