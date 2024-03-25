import psycopg2

conn = psycopg2.connect(
            dbname="postgress",
            user="postgress",
            password="postgress",
            host="12312.12341.111",)

cursor = conn.cursor()

conn.commit()

def read_all_users():
    cursor.execute('SELECT * FROM postgress')
    rows = cursor.fetchall()
    return rows

def read_user_by_id(user_id):
    cursor.execute('SELECT * FROM postgress WHERE id=?', (user_id,))
    row = cursor.fetchone()
    return row

def insert_user(name, email):
    cursor.execute('INSERT INTO postgress (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    return cursor.lastrowid  

def delete_user(user_id):
    cursor.execute('DELETE FROM postgress WHERE id=?', (user_id,))
    conn.commit()

if __name__ == '__main__':
    user_id = insert_user('John Doe', 'johndoe@example.com')
    print(f'Добавлен пользователь с id={user_id}')

    all_users = read_all_users()
    print('Все пользователи:')
    for user in all_users:
        print(user)

    user = read_user_by_id(user_id)
    print('Найден пользователь:')
    print(user)

    delete_user(user_id)
    print(f'Пользователь с id={user_id} удален')


conn.close()
