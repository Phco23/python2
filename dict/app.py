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
        users.append({"name": name, "age": age})
    
    print(users)
    
    element = input("Enter the key for the new element: ")
    length = len(users)
    
    for i in range(length):
        some = input(f"Enter value for element: ")
        users[i].update({element: some}) 
    
    print(users)    

    sort = sorted(users, key=lambda x:x['age'], reverse=True) 
    
    print(sort)


if __name__ == "__main__":
    dict()