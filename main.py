from someClass.someClass import SomeClass
from anotherClass.anotherClass import AnotherClass
from operations.operations import SingleNumberOperations
x = SomeClass('joe', 20)

x.doSomething(10)

nums = AnotherClass(10,3,4,3,89,100,70)

print('the largest number is: ', nums.find_max())
print('the smallest number is: ', nums.find_min())
print(nums)

x = SingleNumberOperations(10)
y = SingleNumberOperations(3)
print(f'x is {x}, y is {y}')
print('x + y is: ', x + y)
print('x - y is: ', x - y)
print('x * y is: ', x * y)
print('x / y is: ', x / y)
