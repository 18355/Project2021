import time
import sqlite3

DATABASE_FILE = "backpack2021.db"            #Link to file

'''functions'''

'''      showing backpack    '''
def show_backpack(connection):                #only print the backpack items 
    try:
        cursor = connection.cursor()              #link to sql
        sql = "SELECT * FROM contents"            #Select all from the SQL data
        cursor.execute(sql)
        results = cursor.fetchall()               
        
        print("\n This is the list of items\n")
        print("  ID        Name         cost          description")
        print("~~~~~~    ~~~~~~~       ~~~~~~~       ~~~~~~~~~~~~~~\n")  

        for item in results:      #loop of printing each item begins
            print(f"{item[0]:<10}{item[1]:<15}{item[2]:<13}{item[3]:<15}")   #leaving spaces between each components
            
        print("~~~~~~    ~~~~~~~       ~~~~~~~       ~~~~~~~~~~~~~~")
    except:
        print("Something wrong happend")

'''       Adding item    '''
def add_item(connection, item_name, item_cost, item_description):       #makes the user add an item to the backpack list
    try:

        cursor = connection.cursor()
        sql = "INSERT INTO contents(name,cost,description) VALUES (?,?,?)"
        cursor.execute(sql,(item_name, item_cost, item_description))
        connection.commit()
    except:
        print("Couldn't add item for some reason")

'''     deleting an item     '''
def delete_item(connection, item_name):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM contents WHERE name = ?"
        cursor.execute(sql,(item_name,))
        row_affect = cursor.rowcount
        if row_affect ==0:
            print("cant find item")
        else:
            connection.commit()
    except:
        print("Item doesn't exist")

def update_description(connection, item_name, new_description):
    try:
        cursor = connection.cursor()
        sql = "UPDATE contents SET description =? WHERE name =?"
        cursor.execute(sql,(new_description, item_name))
        row_affect = cursor.rowcount
        if row_affect ==0:
            print("cant update item")
        else:
            connection.commit()
    except:
        print("failed to update")

while True:                                                    #loop starts 

    with sqlite3.connect(DATABASE_FILE) as connection:                     #connect to sql
        time.sleep(0.5)
        show_backpack(connection)
        selection = input("\nWhat do you want to do with the list? \n A.)Print backpack B.)Add an item C.)Remove an item D.)Update the detail\n\n").upper()
        if selection == "A":             #show items
            show_backpack(connection)
        elif selection == "B":         #add items
            user_add_name = input("What item do you want to add?")
            user_add_cost = input("what is the price?")
            user_add_description = input("give a description")

            add_item(connection, user_add_name, user_add_cost, user_add_description)

        elif selection == "C":             #delete items
            user_delete = input("what do you want to delete?")
            delete_item(connection, user_delete)
        elif selection == "D":             #update items
            user_update_name = input("what item do you want to update?")
            user_update_description = input("what is the new description?")
            update_description(connection, user_update_name, user_update_description)
        else:
            print("???\n please type A, B, C, or D")
