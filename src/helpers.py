import random
import string
import socket


def random_string(lenght=10):
    return "".join([random.choice(string.ascii_letters) for _ in range(lenght)])


def random_digits(lenght=10):
    return "".join([random.choice(string.digits) for _ in range(lenght)])


def random_password(lenght=10):
    string_half_len = lenght // 2
    digits_half_len = lenght - string_half_len
    return random_string(string_half_len) + random_digits(digits_half_len)


def random_email():
    return random_string() + "@" + random_string(5) + "." + random.choice(["com", "ua", "org", "ru"])


def get_user_from_db(connection, firstname, lastname):
    """This user will have password test"""
    query = 'SELECT * FROM oc_customer WHERE firstname = %s AND lastname = %s'
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, (firstname, lastname))
    result = cursor.fetchall()
    cursor.close()
    return result[0]


def delete_user_from_db(connection, firstname, lastname):
    """This user will have password test"""
    query = 'DELETE FROM oc_customer WHERE firstname = %s AND lastname = %s'
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, (firstname, lastname))
    cursor.close()
