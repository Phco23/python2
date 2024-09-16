def listexample():
    print("List example")
    list_exp = [1, 2, 3]
    print(f"List print: {list_exp}")
    print(f"List first element: {list_exp[0]}")
    print(f"List last element: {list_exp[-1]}")
    list_str = ["Hello", "world!"]
    print(f"List string {list_str}")
    list_mix = ["Hello", "world", 123] # Different between python than other language(C#, java, ...)
    print(f"List mix {list_mix}")

def list_example_01():
    list_exp = [1, 2, 3]
    for i in list_exp:
        print(f"Element: {i}")

def list_example_02():
    list_exp = [1, 2, 3]
    i = 0
    while(i < len(list_exp)):
        print(f"Element i {i} = {list_exp[i]}")
        i = i + 1

def list_example_03():
    list_exp = [100, 20, 333]
    num = int(input("Enter number: "))
    list_exp.append(num)
    for i in list_exp:
        print(f"Element: {i}")

def list_example_04():
    # remove, count
    list_exp = [100, 20, 333]
    num_ins = int(input("Enter number to insert: "))
    num = int(input("Enter number: "))
    list_exp.insert(num_ins, num)
    for i in list_exp:
        print(f"Element: {i}")

if __name__ == "__main__":
    list_example_04()