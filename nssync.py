import pymysql as pm

try:
    connection = pm.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '12345',
        database = 'powerdns',
        cursorclass = pm.cursors.DictCursor
    )
    print("connection successul")
    print("#"*20)

    try:
        with connection.cursor() as cur:
            select_zones_table = "SELECT id,notified_serial FROM domains;"
            cur.execute(select_zones_table)

            rows = cursor.fetchall()
            for row in rows:
                print(row)
                print("@"*20)

    finally:
        connection.close()
        print("connection closed")
        print("#"*20)

except Exception as ex:
    print("connections resused")
    pint(ex)
