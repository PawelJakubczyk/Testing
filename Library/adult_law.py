

class Citizen:

    def __init__(self, age: (int or float), criminal_record: bool = False):
        self.age = age
        self.criminal_record = criminal_record

    def is_adult(self) -> bool:
        if type(self.age) not in [int, float]:
            raise ValueError('Wrong Data Type')
        elif self.age >= 18:
            return True
        elif 18 > self.age >= 0:
            return False
        elif self.age < 0:
            raise ValueError("This person don't born yet")

    def law_to_buy_alcohol(self, alcohol_percent: (int or float)) -> bool:
        if (type(self.age) not in [int, float]) or (type(alcohol_percent) not in [int, float]):
            raise TypeError('Wrong Data Type')
        elif alcohol_percent > 100 or alcohol_percent <= 0:
            raise ValueError("This alcohol does not exist")
        elif self.age >= 18:
            return True
        elif self.age >= 16 and alcohol_percent <= 16.5:
            return True
        elif 16 > self.age >= 0:
            return False
        elif self.age < 0:
            raise ValueError("This person don't born yet")

    def vote_law(self) -> bool:
        if type(self.criminal_record) != bool:
            raise TypeError('Wrong Data Type')
        elif self.criminal_record:
            return False
        else:
            return self.is_adult()

    def law_to_buy_weapon(self) -> bool:
        if type(self.criminal_record) != bool:
            raise TypeError('Wrong Data Type')
        elif self.criminal_record:
            return False
        elif type(self.age) not in [int, float]:
            raise ValueError('Wrong Data Type')
        elif self.age >= 21:
            return True
        elif 21 > self.age >= 0:
            return False
        elif self.age < 0:
            raise ValueError("This person don't born yet")

