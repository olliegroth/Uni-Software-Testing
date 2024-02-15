class Person:

    def __init__(self, age, studentStatus):
        self.age = age
        self.studentStatus = studentStatus

    def checkTicket(self):

        ticketCost = 4
        if self.age < 3 or self.age >= 65:
            ticketCost = 0

        if self.studentStatus:
            ticketCost = 2

        return ticketCost