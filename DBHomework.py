import psycopg2
from psycopg2 import Error

conn = psycopg2.connect(database= 'DBHomework', user= 'postgres', password= '33224659LAStill')

def create_database():
    with conn.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS phones (
                id SERIAL PRIMARY KEY,
                client_id INTEGER,
                phone VARCHAR(20) NOT NULL,
                FOREIGN KEY (client_id) REFERENCES clients (id) ON DELETE CASCADE
            )
        ''')


def add_client(first_name, last_name, email):
    with conn.cursor() as cursor:
        cursor.execute('''
            INSERT INTO clients (first_name, last_name, email)
            VALUES (%s, %s, %s)
        ''', (first_name, last_name, email))


def add_phone(client_id, phone):
    with conn.cursor() as cursor:
        cursor.execute('''
            INSERT INTO phones (client_id, phone)
            VALUES (%s, %s)
        ''', (client_id, phone))


def update_client(client_id, first_name=None, last_name=None, email=None):
    with conn.cursor() as cursor:
        if first_name:
            cursor.execute('''
                UPDATE clients
                SET first_name = %s
                WHERE id = %s
            ''', (first_name, client_id))

        if last_name:
            cursor.execute('''
                UPDATE clients
                SET last_name = %s
                WHERE id = %s
            ''', (last_name, client_id))

        if email:
            cursor.execute('''
                UPDATE clients
                SET email = %s
                WHERE id = %s
            ''', (email, client_id))


def delete_phone(phone_id):
    with conn.cursor() as cursor:
        cursor.execute('''
            DELETE FROM phones
            WHERE id = %s
        ''', (phone_id,))


def find_client(search_term):
    with conn.cursor() as cursor:
        cursor.execute('''
            SELECT c.id, c.first_name, c.last_name, c.email, p.phone
            FROM clients c
            LEFT JOIN phones p ON c.id = p.client_id
            WHERE c.first_name LIKE %s OR c.last_name LIKE %s OR c.email LIKE %s OR p.phone LIKE %s
        ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))


if __name__ == "__main__":
    create_database()
    add_client('Иван', 'Иванов', 'kserngui@mail.com')
    add_client('Илья', 'Иванов', 'gull@mail.com')
    add_phone(1, '8907246231')
    add_phone(2, '8902351234')
    add_phone(1, '8989754896')
    update_client(1, 'Ваня')
    delete_phone(2)
    find_client('Ваня')

conn.commit()
conn.close()
