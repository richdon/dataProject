class AnotherClass:
    def __init__(self, *args):
        self.numbers = args

    def find_max(self):
        return max(self.numbers)

    def find_min(self):
        return min(self.numbers)

    def __repr__(self):
        return f'numbers are {self.numbers}'