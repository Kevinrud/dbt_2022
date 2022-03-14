import sqlite3
import pandas as pd
from tabulate import tabulate

LIST_CUSTOMERS = """SELECT customerno as Kundnummer, first_name as Förnamn, 
last_name as Efternamn, street_name as Gata, town as Stad, 
zip as Postnummer, country as Land, email as Epost, phone as Telefonnummer
 FROM customer"""

LIST_ORDERS = """SELECT orderno as Ordernummer, orders.customerno as Kundnummer,
order_date as Orderdatum, first_name as Förnamn, last_name as Efternamn,
street_name as Gata, town as Stad, zip as Postnummer 
FROM orders JOIN customer ON orders.customerno = customer.customerno"""


def list_data(sqlstr):
    con = sqlite3.connect("datastore/ovning.db")
    cursor = con.cursor()
    cursor.execute(sqlstr)
    datat = cursor.fetchall()
    columns = list(map(lambda x: x[0], cursor.description))  # Från cursor hämta alla kolumn namn till en lista
    # Följande pandas settings behövs inte om man använder tabulate.
    # pd.set_option('max_colwidth', None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.expand_frame_repr', False)
    dataframe = pd.DataFrame(datat, columns=columns)
    print(tabulate(dataframe, showindex=False, headers=columns))
    con.close()


def main():
    inp = ""
    while inp != "quit":
        inp = input(">")
        if inp == "list customers":
            list_data(LIST_CUSTOMERS)
        if inp == "list orders":
            list_data(LIST_ORDERS)


if __name__ == '__main__':
    main()
