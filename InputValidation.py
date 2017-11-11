import argparse
import re
import sqlite3
import sys
from sqlite3 import Error


def check_name(name_string):
    test_name = name_regex_pattern.match(name_string)
    if test_name:
        return True
    else:
        return False


def check_phone(number_string):
    test_number = phone_number_regex_pattern.match(number_string)
    if test_number:
        return True
    else:
        return False


def create_connection():
    """ create a database connection to a database on the specified path
    """
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except Error as e:
        print(e)

    return None


# function to add members to the Database
def add_member(conn, name, phone):
    query = "INSERT INTO members (name, phone) VALUES (?,?);"
    cur = conn.cursor()
    cur.execute("INSERT INTO members (name, phone) VALUES (?,?);", (name, phone))
    conn.commit()


# function to list all the members in the database
def list_members(conn):
    cur = conn.cursor()
    cur.execute("SELECT name,phone FROM members;")

    rows = cur.fetchall()
    for row in rows:
        print(row)


# function to delete a member from the database
def delete_member(conn, value):
    cur = conn.cursor()
    cur.execute("SELECT name,phone FROM members WHERE name = '" + value + "' OR phone = '" + value + "';")

    rows = cur.fetchall()
    if len(rows):
        test = cur.execute("DELETE FROM members WHERE name = '" + value + "' OR phone = '" + value + "';")
        conn.commit()
    else:
        sys.stderr.write("Entry not available in database!")


# function to check the input command
def regex_check():
    usage_message = 'InputValidation.py command\nCommands:\n' \
                    'ADD "<person>" "<phone #>",\nDEL "<person>",\n' \
                    'DEL "<phone #>", \nLIST'

    help_message = 'ADD "<person>" "<phone #>",\nDEL "<person>",\n' \
                   'DEL "<phone #>", \nLIST'

    # parse the command entered by the user
    parser = argparse.ArgumentParser(usage=usage_message, description='Process some commands.')
    parser.add_argument('command', nargs='+', help=help_message)
    args = parser.parse_args()
    user_input = (args.command)

    # connect to the database
    conn = create_connection()
    if conn is not None:
        if user_input[0] == "LIST" and len(user_input) == 1:
            print("####list####")
            list_members(conn)
        elif user_input[0] == "DEL" and len(user_input) == 2:
            value = str(user_input[1])
            test_name = check_name(value)
            test_phone = check_phone(value)
            if test_name or test_phone:
                delete_member(conn, value)
            else:
                sys.exit(1)
        elif user_input[0] == "ADD" and len(user_input) == 3:
            name = str(user_input[1])
            phone = str(user_input[2])
            test_name = check_name(name)
            test_phone = check_phone(phone)

            if test_name:
                if test_phone:
                    add_member(conn, name, phone)
                    sys.exit(0)
                else:
                    sys.stderr.write("Invalid Phone Number")
                    sys.exit(1)
            else:
                sys.stderr.write("Invalid Name")
                sys.exit(1)
        else:
            sys.stderr.write("Invalid Command. Try -h option for help")
            sys.exit(1)


if __name__ == '__main__':
    # path to Database file
    db_path = 'C:\sqlite\members.db'

    # regular expression for validating name
    name_regex_string = "^[A-Z]\\'?([a-zA-Z]*?\\'?[a-zA-Z]*?\\,?[ ]?\\'?\\-?\\.?){1,3}$"
    name_regex_pattern = re.compile(name_regex_string)

    # regular expression for validating phone#
    phone_number_regex_string = "(^\\d{5}$)|(^\\d{5}\\.\\d{5}$)|(^\\+[1-9]{1,2}[ ]?\\(|^[1][ ]?\\(|^[0][1][1][ ][1]?[ " \
                                "]?\\(?|^\\(?)([1-9]\\d{1,2})?\\)?[- ]?(\\d{3})[-| ](\\d{4})$";
    phone_number_regex_pattern = re.compile(phone_number_regex_string)

    regex_check()
