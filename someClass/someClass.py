class SomeClass:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def doSomething(self, times):
        while times > 0:
            print('name is: ', self.name, 'value is: ', self.value )
            self.value -= 1
            times -= 1