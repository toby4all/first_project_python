import json

import pymysql

def add_user(user_id, username):
    schema_name = 'myDb'
    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting data into table
    cursor.execute(f"INSERT into {schema_name}.users (name, id) VALUES ('{username}', {user_id})")

    cursor.close()
    conn.close()

def get_user(user_id):
    schema_name = 'myDb'
    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Insert data into table
    cursor.execute(f"SELECT name FROM {schema_name}.users WHERE user_id =({user_id}) ")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None
    cursor.close()
    conn.close()

def update_user(user_id, username):
    schema_name = 'myDb'
    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()
    cursor.execute(f"UPDATE * {schema_name}.users SET name = {username} WHERE user_id = {user_id}")
    cursor.close()
    conn.close()

def delete_user(user_id):
    schema_name = 'myDb'
    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {schema_name}.users WHERE user_id = '{user_id}'")

    cursor.close()
    conn.close()
