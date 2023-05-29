import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS clients_db(
            client_id PRIMARY KEY,
            first_name VARCHAR(40) UNIQUE,
            last_name VARCHAR(40) UNIQUE,
            email VARCHAR(40) UNIQUE,
            phone INTEGER NOT NULL
        );
        """)
        conn.commit()


def add_client(conn, first_name, last_name, email, phone=None):
    with conn.cursor() as curs:
        if find_client(conn, email=email):
            return "Client with this email already exists"
        curs.execute(
                """
                INSERT INTO clients_db (first_name, last_name, email) 
                VALUES (%s, %s, %s) RETURNING (client_id); 
                """,
                (first_name, last_name, email)
            )
        if ...:  # как проверить передали ли телефон при добавлении контакта ?
                client_id = curs.fetchone()[0]
                add_phone(conn, client_id, phone)
                conn.commit()


def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
            UPDATE clients_db SET phone=%s WHERE client_id=%s;
            """, (phone, client_id))
        cur.execute("""
            SELECT * FROM clients_db;
            """)
        print(cur.fetchall())


def change_client(conn, client_id, first_name=None, last_name=None, email=None):
    with conn.cursor() as cur:
        cur.execute("""
            UPDATE clients_db SET first_name=%s WHERE id=%s;
            """, ('Python Advanced', python_id))
        cur.execute("""
            SELECT * FROM course;
            """)
        print(cur.fetchall())


def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
           DELETE FROM clients_db WHERE id=%s;
           """, (1,))
        cur.execute("""
           SELECT * FROM homework;
           """)
        print(cur.fetchall())


def delete_client(conn, client_id):
    cur.execute("""
           DELETE FROM clients_db WHERE client_id=%s;
           """, (1,))
    cur.execute("""
           SELECT * FROM homework;
           """)
    print(cur.fetchall())

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
        cursor.execute("""
        SELECT id FROM clients_db WHERE first_name=%s;
        """, (first_name,))
        return cur.fetchone()[0]

    python_id = get_course_id(cur, 'Python')
    print('python_id', python_id)


with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
    pass


