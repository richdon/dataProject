from someClass.someClass import SomeClass
from anotherClass.anotherClass import AnotherClass
x = SomeClass('joe', 20)

x.doSomething(10)

nums = AnotherClass(10,3,4,3,89,100,70)

print('the largest number is: ', nums.find_max())
print('the smallest number is: ', nums.find_min())
print('all the numbers are: ', nums)