import mysql.connector

def insertProduct(name,price,imageUrl,description):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mysql1234",
        database = "node-app"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"Son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")


def insertProducts(list):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mysql1234",
        database = "node-app"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"Son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")


list = []
while True:
    name = input("Ürün adı: ")
    price = float(input("Ürün fiyatı: "))
    imageUrl = input("Ürün resim linki: ")
    description = input("Ürün açıklaması: ")

    list.append((name,price,imageUrl,description))

    result = input("Devam etmek istiyor musunuz? (e/h)")
    if result == "h":
        print("Kayıtlarınız veritabanına aktarılıyor.")
        print(list)
        insertProducts(list)
        break


# insertProduct(name,price,imageUrl,description)