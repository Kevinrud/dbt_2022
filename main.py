import sqlite3

# TODO anslut till databasen
# TODO Skriv ut alla kunder
# TODO Skriv ut alla ordrar

LIST_CUSTOMERS = "SELECT customerno, first_name, last_name, street_name, town, zip, country, email, phone FROM customer"

def main():
    inp = ""
    while inp != "quit":
        inp = input(">")
        if inp == "list customers":
            con = sqlite3.connect("datastore/ovning.db")
            cursor = con.cursor()
            cursor.execute(LIST_CUSTOMERS)
            for customer in cursor:
                # TODO skriv ut kunddatan på ett snyggare sätt
                print(customer)
            con.close()
        if inp == "list orders":
            # TODO skriv ut ordrar
            # ordernummer, kundnummer, orderdatum, förnamn, efternamn, adress
            print("FIXME")


if __name__ == '__main__':
    main()