from testDrivenDevelopment.person import Person

def test_normal_ticket():
    normalPerson = Person(23, False)
    normalPerson.checkTicket()
    assert normalPerson.checkTicket() == 4