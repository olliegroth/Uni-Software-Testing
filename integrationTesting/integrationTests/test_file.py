from integrationTesting.Dog import Dog
from integrationTesting.Enclosure import Enclosure
from integrationTesting.Kennel_Company import Kennel_Company
import pytest

@pytest.fixture
def create_kennel(monkeypatch):
    monkeypatch.setattr(Kennel_Company, "load_enclosures", load_enclosure_stub())
    myKennelCompany = Kennel_Company()
    return myKennelCompany

def load_enclosure_stub():
    return [
        Enclosure(1, 30, 3)
    ]

def test_book_dog(monkeypatch, create_kennel):

    Jed = Dog("Jed", "Ollie", 11,"Lab", "No notes")
    Sam = Dog("Sam", "Dan", 2, "Dalmatian", "Very loud")
    create_kennel.book_dog(Jed)
    create_kennel.book_dog(Sam)

    assert create_kennel.spaces_left() == 1