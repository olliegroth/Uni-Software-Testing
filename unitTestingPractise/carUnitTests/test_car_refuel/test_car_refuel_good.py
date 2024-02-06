from unitTestingPractise.car import Car

def test_refuel():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 50, 102, 50)
    firstCar.refuel(20)
    assert firstCar.fuelLevel == 70