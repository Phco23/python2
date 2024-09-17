def dict_example():
    person = [
        {
            "name": "Nguyen Van A",
            "age": 10,
            "address": "Hanoi"
        },
        {
            "name": "Nguyen Van B",
            "age": 10,
            "address": "Hanhanoi"
        },
        {
            "name": "Nguyen Van C",
            "age": 10,
            "address": "d"
        },
    ]
    print(person)
    print(f"Name: {person[1]['name']}")

def dict():
    users = []
    for i in range(10):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        users.append({"name": name,"age": age})
    print(users)
    element = input("Enter one more element: ")
    for i in range(10):
        some = input("Enter something: ")
        users.append({"name": name,"age": age, element: some})
    print(users)
    


if __name__ == "__main__":
    dict()