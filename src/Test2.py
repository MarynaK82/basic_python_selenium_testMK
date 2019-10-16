import math
print("Hello")

name:str = "Alex"
height:int = 180
weight:float = 83.5

print(name + " " + name)
print(name + str(height))
print(height + weight)
print(height + int(weight))

height = height + 6
height +=6
print(name + " is " + str(height) + " cm and " + str(weight) + " kg")

age = 13
if (age < 10):
    print("Less 10 years Child")
elif (age < 19):
    if(age == 13):
        print("small")
    print("teenager")
elif (age == 100):
    print("grandma")
else:
    print("retire")

list = [12, 44.3, 'd', ['h', 'i']]
list.append('new')
list.insert(1, 12)

print(list[3])
print(list[3][0])
print(list)

for element in list:
    print(element)

list.remove(44.3)
print(list)

set = {'Alex', 12, 12, 'Peter'}
print(set)

cortage = ('Alex', 12, 12, 'Peter')
print(cortage)

dictionary = {'name' : 'Alex', 'profession' : 'Automation', 'age' : 100}
print (dictionary)

d = {'name' : {'first' : 'Alex', 'last' : 'Kardash'}, 'profession' : 'Automation', 'age' : 100}
print (d['profession'])
print (d['name']['first'], d['age'])
print(d)


def summa(a, b, c):
    return (a + b + c)
print(summa(3, 7, 8))