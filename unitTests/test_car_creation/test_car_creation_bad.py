from car import Car

def test_car_creation():
    firstCar = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 0, 102, 100)
    assert firstCar.make != "Porsche"
    assert firstCar.model != "944"
    assert firstCar.numPlate != "OG23 SEP"
    assert firstCar.doors != 6
    assert firstCar.wheels != 6
    assert firstCar.engineSize != 2.5
    assert firstCar.currentSpeed != 100
    assert firstCar.maxSpeed != 140
    assert firstCar.fuelLevel != 0