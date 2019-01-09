#Create a python dictionary for phones and their prices. Write functions to
  #a. Add a new entry (phone:price)
  #b. Search for a particular phone and retrieve it’s price
  #c. Find phones with same price
  #d. Remove an entry.
  #e. Display all phones sorted according to price. [Program must be menu driven]

phones = dict()


def addentry():
    global phones
    name = input("Enter name of the phone ")
    price = input("Enter price")
    phones.update({name: price})


def search_by_name(name1):
    global phones
    for key, value in phones.items():
        if name1 == key:
            print("Found, its price is ", value)


def search_by_price(name1):
    global phones
    for key, value in phones.items():
        if name1 == value:
            print("Found, name of the phone is ", key)


def group_by_price():
    global phones
    pricelist = sorted(phones.values())
    pricelist = list(set(pricelist))  # removes duplicate values
    pricelist.append(None)
    print("Phones grouped by same prices are ")
    
    #while pricelist[0] != None:
    while pricelist[0] is not None:
        for key, value in phones.items():
            if value == pricelist[0]:
                print(key, end=',')
        print('')
        del (pricelist[0])


def remove_entry():
    global phones
    print("Enter name of phone to delete ")
    name = input();
    try:
        del (phones[name])
        print(phones.keys())
    except:
        print("Entry not found")


def sortdict():
    print(sorted(phones.items(), key=lambda x: x[1]))


while True:
    print("Enter 1 to add entry, \n2 to search by name, \n3 to search by price,\n4 to group by price, \n5 to sort,\n6 to delete entry, 0 to exit\n")
    choice = int(input())
    if choice == 1:
        addentry()
    elif choice == 2:
        name = input("Enter name of the phone")
        search_by_name(name)
    elif choice == 3:
        price = input("Enter name of the phone")
        search_by_price(price)
    elif choice == 4:
        group_by_price()
    elif choice == 5:
        sortdict()
    elif choice == 6:
        remove_entry()
    else:
        break
