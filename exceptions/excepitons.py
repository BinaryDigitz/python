# Handle exception with try and catch
numbers = [*range(5)]

try:
   
    print('File open')
    age = int(input('age: '))
    xfactor = 10 / age
    print(age)
except (ValueError,ZeroDivisionError):
    print(" You didn't enter the right age.....")

else:
    print('No exception were thrown.')


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age must be greater than 0')
    return 10 / age
try:
    calculate_xfactor(-1)
except ValueError as ex:
    print(ex)

    # BETTER APPROACH I S RAISING EXCEPITONS
    