from unitTesting.car import Car

def test_brake():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 50, 102, 100)
    firstCar.brake(20)
    assert firstCar.currentSpeed == 30