plus = lambda a,b: a + b

if __name__ == "__main__":
    print(f"lambda: {plus(1, 2)}")

def evenNumber():
    numbers = [1, 2, 5, 11, 6, 9, 3]
    for i in numbers:
        if(i % 2 != 0):
            print(i)

if __name__ == "__main__":
    # evenNumber()

    numbers = []
    for i in range(6):
        number = int(input("Input number: "))
        numbers.append(number)
    evenNum = list(filter(lambda x:x%3 == 0, numbers))
    print(evenNum)
    sort = list(sorted(numbers, key=lambda x:x))
    print(f"Order asc {sort}")
    sort_desc = list(sorted(numbers, key=lambda x:x, reverse=True))
    print(f"Order desc {sort_desc}")
    print(f"Largest number: {max(numbers)}")
    print(f"Lowest number: {min(numbers)}")