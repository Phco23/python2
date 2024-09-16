print("Hello World")
def sum(a, b):
    total = a + b
    print(f"Summary of 2 numbers: {total}")

def sum_array():
    total = 0
    for i in range(10):
        total_temp = total
        total = total_temp + i
        print(f"Array possition {i}: {total_temp} + {i} = {total}")
    print(f"Total array: {total}")


def div(a, b):
    result = a/b
    print(f"Div 2 numbers: {result}")

def sub(a, b):
    result = a - b
    print(f"Sub 2 number {result}")    

def mul(a, b):
    result = a * b
    print(f"Mul 2 number {result}") 

def loop_example():
    for i in range(10, 0, -1):
        print(f"i = {i}")

def loop_example_01():
    x = 0
    while (x < 10):
        x = x + 1
        print(f"x = {x}")
    print("End loop")

def loop_example_02(x):
    match x:
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("There")   
        case _:
            print("Default")

def test():
    array = [1, 3, 10, 7, 5, 11, 6, 4]
    print(f"Before: {array}")
    find = []
    for i in array:
        if i % 2 != 0:
            find.append(i)
    print(f"After: {find}")

def test2():
    size = int(input("Enter size of array: "))
    array = []
    for i in range(size):
        number = int(input("Enter number: "))
        array.append(number)     
    print(array)
    
def menu():
        while(True):
            try:
                choice = int(input("Enter choice: "))
                a = int(input("Enter num 1: "))
                b = int(input("Enter num 2: "))
                if choice == 1:
                    sum(a, b)
                if choice == 2:
                    div(a,b)
                if choice == 3:
                    sub(a,b)
                if choice == 4:
                    mul(a,b) 
                if choice == 5:
                    sum_array()   
                if choice == 6:
                    loop_example()
                if choice == 7:
                    loop_example_01()
                if choice == 8:
                    loop_example_02(a)
                if choice == 9:
                    test()
                if choice == 10:
                    test2()
                else:
                    print("Wrong number")
            except:
                print("Only number are available")
                break

if __name__ == "__main__":
    menu()