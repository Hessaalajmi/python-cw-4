def my_name():
    print("My name is Hessa")
my_name()

def my_meal(food, drink):
    print(f'I like to eat {food} while drinking {drink}')
my_meal('sandwich', 'water')

def cube(number):
    return number**3 


def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False           

x = cube(7)
print(x)

y = by_three(7)
print(y)
