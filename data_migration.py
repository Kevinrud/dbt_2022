import mariadb
import pymongo



# Testa att ansluta mot MariaDB och läsa kunddata
# 1. Ansluta
# 2. Skriv en query
# 3. Kör query och printa resultatet
from db_config import HOST, PORT, DBUSER, DBPASS, DBNAME


def read_customers():
    connection: mariadb.connection = mariadb.connect(
        host=HOST,
        port=PORT,
        user=DBUSER,
        password=DBPASS,
        database=DBNAME
    )
    # 1. Skapa en cursor
    cur = connection.cursor()
    # 2. Kör en query
    cur.execute("SELECT * FROM customers")
    # 3. Iterera över resultatet och skriv ut
    for r in cur:
        print(r)
    # 4. Stäng cursor
    cur.close()
    # 5. Stäng anslutningen
    connection.close()


# read_customers()
def read_write_customers_mongo():
    #  Testa att ansluta mot MongDB, läsa lite data, skriva data
    # 1. Anslut mot mongodb
    client = pymongo.MongoClient('mongodb://localhost')
    # 2. "Välj" databas, skapa ett objekt som refererar till en viss databas
    db = client['pvt21']
    # 3. "Välj" collection, skapa ett objekt som refererar till en collection, customers i det här fallet
    customers = db['customers']
    # 4. Läs data och skriv ut
    kunden = customers.find_one({"customerno": 1})
    print(kunden['first_name'])
    print(kunden['last_name'])
    testobjekt = {'_id': 5, 'en_nyckel': 'Ett värde som vi sparar', 'foo': 12414}
    foo = db['foo']
    foo.insert_one(testobjekt)
    client.close()


def migrate_customers():
    #  Migrera kunddata från MariaDB till Mongodb
    # 1. Anslut till Mariadb
    connection: mariadb.connection = mariadb.connect(
        host=HOST,
        port=PORT,
        user=DBUSER,
        password=DBPASS,
        database=DBNAME
    )
    cur = connection.cursor()
    client = pymongo.MongoClient('mongodb://localhost')
    db = client['pvt21']
    customers = db['customers']
    # 2. Läs kunddata från Mariadb
    cur.execute('SELECT * FROM customers')
    # 3. Bygg en python dict av varje kund
    for r in cur:
        customer_dict = {
            '_id': r[0],
            'first_name': r[1],
            'last_name': r[2],
            'email': r[3],
            'gender': r[4],
            'country': r[5],
            'city': r[6],
            'street_address': r[7]
        }
        # 4. Spara kund-dicten i Mongodb
        customers.insert_one(customer_dict)
    cur.close()
    connection.close()


# TODO Migrera produktdata från MariaDB till Mongodb
#   Om ni får problem med decimalkonvertering kan istället konvertera priset till float
#
# TODO Migrera ordrar från MariaDB till Mongodb
#   TODO Ta fram en struktur för orderdata i Mongodb, hur vill vi att datan
#    skall se ut
#   TODO skriv SQL-queries för att hämta orderdata från MariadDB