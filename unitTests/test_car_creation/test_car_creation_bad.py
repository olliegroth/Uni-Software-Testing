import pytest
from car import Car

def test_incorrect_car_details():
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

def test_numPlate_out_of_range():
    with pytest.raises(Exception) as numPlateError:
        Car("Skoda", "Fabia", "012345678910", 5, 4, 1.2, 50, 102, 50)
    assert str(numPlateError.value) == "Number plate length cannot exceed 10"

def test_doors_out_of_range():
    with pytest.raises(Exception) as doorsError:
        Car("Skoda", "Fabia", "GR07 THO", -1, 4, 1.2, 50, 102, 50)
    assert str(doorsError.value) == "Minimum amount of doors is 0"

def test_wheels_out_of_range():
    with pytest.raises(Exception) as wheelsError:
        Car("Skoda", "Fabia", "GR07 THO", 5, 2, 1.2, 50, 102, 50)
    assert str(wheelsError.value) == "Minimum amount of wheels is 3"

def test_currentSpeed_out_of_range():
    with pytest.raises(Exception) as currentSpeedError:
        Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 200, 102, 50)
    assert str(currentSpeedError.value) == "Current speed cannot be more than Max speed"

def test_fuelLevel_out_of_range():
    with pytest.raises(Exception) as fuelLevelError:
        Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 50, 102, 200)
    assert str(fuelLevelError.value) == "Fuel level (%) cannot exceed 100"