import psycopg2
import csv

datab = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="postgres1234",  
    host="localhost"
)
cur = datab.cursor()
def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (name, phone))
    datab.commit()
    print("import comleted")
def insert_from_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
    datab.commit()
def update_user():
    name=input("input name where number have need to change: ")
    new_phone=input("new phone number: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, name))
    datab.commit()
    print("number updated")
def search():
    pattern = input("input anny part of a number: ")
    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", ('%' + pattern + '%',))
    for row in cur.fetchall():
        print(row)
def deletes():
    key=input("delete by number or name: ")
    cur.execute("DELETE FROM phonebook WHERE username=%s OR phone=%s", (key, key))
    datab.commit()
    print("deleted")
def nev_menu():
    while True:
        print("1 - insert \n")
        print("2 - from csv\n")
        print("3 - update\n")
        print("4 - search by any part of a number\n")
        print("5 - delete\n")
        print("0 - exist\n")
        choice = input("Выберите опцию: ")
        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv("contacts.csv")
        elif choice == '3':
            update_user()
        elif choice == '4':
            search()
        elif choice == '5':
            deletes()
        elif choice == '0':
            break

nev_menu()
cur.close()
datab.close()

    