# noinspection PyUnresolvedReferences

class Insurance:
    # insured = []

    def __init__(self, name=zdenek, surname=kunc, age=55, telefon=769582741,):
        self.insurance = [name, surname, age, telefon]

insurance = Insurance(name, surname, age, telefon)


def append_insured(self, insurance):
    self.insurance.append(insurance)
