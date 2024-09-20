import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dwhdahdhadha"
    )

def add_student():
    name = input("Enter name: ")    
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    connection = connect_to_db()
    cursor = connection.cursor()

    insert_query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, age, grade))

    connection.commit()
    print(f"Add student {name}!")
    

    connection.close()

def update_student():
    id = input("Enter id: ")
    name = input("Enter new name: ")
    connection = connect_to_db()
    cursor = connection.cursor()

    update_query = "UPDATE students SET name = %s WHERE id=%s"
    cursor.execute(update_query, (name, id))

    connection.commit()
    print(f"Update student {name}!")

if __name__ == "__main__":
    update_student()