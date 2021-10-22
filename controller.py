# Controller va a hacer los query para la base de datos
from db import get_connection_db


# creo una funcion para crear un empleado
def insert_employee(name, last_name, email, position):
    #  Instancio mi connection
    connection = get_connection_db()

    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO employees(name, last_name, email, position) VALUES(%s, %s, %s, %s)",
            (name, last_name, email, position)
        )
    connection.commit()
    connection.close()


def get_employees():
    connection = get_connection_db()
    # SELECT
    # creo un array de employees
    employees = []

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, name, last_name, email, position FROM employees")
        employees = cursor.fetchall()
    connection.close()

    return employees
