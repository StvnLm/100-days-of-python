import sys
from HomeInventory import Database

def main_main():
    menu = {}
    menu["1"] = "Add Room"
    menu["2"] = "Add Inventory"
    menu["3"] = "View Inventory"
    menu["4"] = "Total Value"
    menu["5"] = "Exit"

    while True:
        print("\n")
        for item, desc in sorted(menu.items()):
            print(str(item) + '.', desc)

        choice = input("Selection: ")
        if choice == "1":
            add_room()
        elif choice == "2":
            add_inventory(check_input())
        elif choice == "3":
            view_inventory(check_input())
        elif choice == "4":
            calc_total()
        elif choice == "5":
            sys.exit()
        else:
            print("Invalid Option, try again.")


def scrub(table_name):
    return ''.join(chr for chr in table_name if chr.isalnum())


def check_input():
    while True:
        print("\n")
        for room in list_rooms():
            print(room)
        selection = input("Select a room: ").lower()
        if selection not in list_rooms():
            print(f"{selection} does not exist")
        else:
            return scrub(selection)


def calc_total():
    total = 0
    room_list = list_rooms()
    with Database.access_db() as cursor:
        for room in room_list:
            cursor.execute("SELECT value FROM " + room)
            for value in cursor:
                total += value[0]
        print(f"Total value of all rooms is ${total}")

def add_inventory(selection):
    while True:
        name = input("\nName of item: ")
        cost = input("Dollar value: ")
        with Database.access_db() as cursor:
            cursor.execute("INSERT INTO " + selection + " VALUES(?, ?)", [name, cost])

        cont = input('\nHit Q to quit or any other key to continue: ')
        if cont.lower() == 'q':
            break


def view_inventory(selection):
    total = 0
    with Database.access_db() as cursor:
        cursor.execute("SELECT * FROM " + selection)
        print("\n")
        for data in cursor:
            print("%s: $%d" % (data[0], data[1]))
            total += data[1]
        print("Total Value: $%d" % total)


def list_rooms():
    room_list = []
    with Database.access_db() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for room in cursor:
            room_list.append(room[0])
        return room_list


def add_room():
    name = input("\nWhat name would you like to give the room?")
    name = scrub(name)
    with Database.access_db() as cursor:
        cursor.execute("CREATE TABLE " + name.lower() + " (Item Text, Value REAL)")
        print(f"\nA room with the name {name} has been addded to the database.")


if __name__ == '__main__':
    Database.first_launch()
    main_main()
