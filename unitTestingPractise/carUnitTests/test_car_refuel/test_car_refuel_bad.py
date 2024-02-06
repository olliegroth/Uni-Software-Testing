from unitTestingPractise.car import Car

def test_zero_refuel_value():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 50, 102, 50)
    firstCar.refuel(0)
    assert firstCar.fuelLevel == 50

def test_negative_refuel_value():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 50, 102, 50)
    firstCar.refuel(-20)
    assert firstCar.fuelLevel == 50

def test_refuel_past_max():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 50, 102, 50)
    firstCar.refuel(75)
    assert firstCar.fuelLevel == 100

def test_refuel_more_than_max_fuel():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 50, 102, 50)
    firstCar.refuel(150)
    assert firstCar.fuelLevel == 50