from testDrivenDevelopment.person import Person

def test_normal_ticket():
    normalPerson = Person(23, False)
    normalPerson.checkTicket()
    assert normalPerson.checkTicket() == 4

def test_under_three_ticket():
    normalPerson = Person(2, False)
    normalPerson.checkTicket()
    assert normalPerson.checkTicket() == 0

def test_elderly_ticket():
    normalPerson = Person(97, False)
    normalPerson.checkTicket()
    assert normalPerson.checkTicket() == 0

def test_student_ticket():
    normalPerson = Person(17, True)
    normalPerson.checkTicket()
    assert normalPerson.checkTicket() == 2