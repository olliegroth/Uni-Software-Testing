from car import Car

def test_brake_past_zero():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 20, 102, 100)
    firstCar.brake(50)
    assert firstCar.currentSpeed == 0

def test_zero_brake_value():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 50, 102, 1)
    firstCar.brake(0)
    assert firstCar.currentSpeed == 50

def test_negative_break_value():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 50, 102, 1)
    firstCar.brake(-20)
    assert firstCar.currentSpeed == 50