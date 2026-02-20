class ValidatedAttribute:
    def __init__(self, min_val):
        self.min_val = min_val

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if value < self.min_val:
            raise ValueError(f"{self.name} must be at least {self.min_val}")
        instance.__dict__[self.name] = value

class Player:
    age = ValidatedAttribute(18)
