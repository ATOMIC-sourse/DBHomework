import psycopg2

conn = psycopg2.connect(database= 'DBHomework', user= 'postgres', password= '33224659LAStill')
cur = conn.cursor()
def creat_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS per_inf(
        id serial primary key,
        name varchar(80) not null UNIQUE,
        last_name varchar(80) not null,
        email varchar(80) not null,
        phone_number int
    )
    """)
    conn.commit()

def add_per(name, last_name, email):
    cur.execute("""
    INSERT INTO per_inf(name, last_name, email) VALUES(%s, %s, %s);
    """, (name, last_name, email))
    conn.commit()

def add_per_num(number):
    cur.execute("""
    INSERT INTO per_inf(number) VALUES(%s);
    """, number)
    conn.commit()

def upd_per(name, last_name, email, number, id):
    cur.execute("""
    UPDATE per_inf SET name=%s, last_name=%s, email=%s, number=%s WHERE id=%s;
    """, (name, last_name, email, number, id))
    conn.commit()

def del_num(number):
    cur.execute("""
    DELETE FROM per_inf WHERE number=%s
    """, number)
    conn.commit()

def del_inf(name, last_name, email):
    cur.execute("""
    DELETE FROM per_inf WHERE name=%s, last_name=%s, email=%s
    """, (name, last_name, email))
    conn.commit()

def sel_per(name, last_name, email, number):
    cur.execute("""
    SELECT name, last_name, email, number FROM per_inf WHERE name=%s, last_name=%s, email=%s, number=%s;
    """, (name, last_name, email, number))
    conn.commit()


creat_table()
add_per(input(), input(), input())
add_per_num(int(input()))
upd_per(input(), input(), input(), input(), input())
del_num(int(input()))
del_inf(input(), input(), input())
sel_per(input(), input(), input(), int(input()))
cur.close()
conn.close()
