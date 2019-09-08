# Followed https://www.youtube.com/watch?v=x7SwgcpACng
import mysql.connector
# update db credentials to work in dev env
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
)

def create_checkdb():
    print(mydb)

    mycursor = mydb.cursor()
    resultCreate = mycursor.execute('CREATE DATABASE IF NOT EXISTS pytest')
    print(resultCreate)

    mycursor = mydb.cursor()
    mycursor.execute('SHOW DATABASES')

    for dbname in mycursor:
        print(dbname)


def create_tables():
    cursor = mydb.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS pytest.students (name VARCHAR(255), age INTEGER (10))")


def insert_students():
    mydb.cursor().execute('DELETE FROM pytest.students')
    sql_formula = "INSERT INTO pytest.students (name, age) VALUES(%s, %s)"
    cursor = mydb.cursor()
    rachel = ("Monica Geller-Bing", 23)
    cursor.execute(sql_formula, rachel)
    mydb.commit()

    cursor = mydb.cursor()
    students = [
        ('Joe Tribbiani', 23),
        ('Chandler Bing', 23),
        ('Phoebe Buffay', 24),
        ('Ross Geller', 22),
        ('Rachel Green', 21),
        ('John Doe', 30)
    ]
    cursor.executemany(sql_formula, students)
    mydb.commit()


def list_students():
    sql = "SELECT name, age FROM pytest.students ORDER BY name"
    cursor = mydb.cursor()
    cursor.execute(sql)
    print('Fetch one')
    result = cursor.fetchone()
    print(result)
    print("Fetch all")
    result = cursor.fetchall()
    print(result)
    cursor.close()


def query_students(word):
    word = "%" + word + "%"
    print('QUERY STUDENTS BY:', word)
    sql = "SELECT name, age FROM pytest.students WHERE name like %s ORDER BY name"
    cursor = mydb.cursor()
    cursor.execute(sql, (word, ))
    result = cursor.fetchall()
    print(result)
    cursor.close()


def update_age(name, age):
    print("set ", name, "age to ", age)
    cursor = mydb.cursor()
    cursor.execute('UPDATE pytest.students SET age = %s WHERE name = %s', (age, name))
    cursor.close()
    query_students(name)


def delete_student(name):
    print("Delete", name)
    cursor = mydb.cursor()
    cursor.execute('DELETE FROM pytest.students WHERE name = %s', (name,))
    mydb.commit()
    cursor.close()


create_checkdb()
create_tables()
insert_students()
list_students()
update_age('John Doe', 10)
query_students('Phoebe')
query_students('Bing')
query_students('Geller')

delete_student('Joe Tribbiani')
delete_student('Rachel Green')
list_students()