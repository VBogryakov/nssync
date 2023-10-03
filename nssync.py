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
        
        list_row = ()
        with connection.cursor() as cursor:
            select_zones_table = "SELECT id,notified_serial FROM domains;"
            cursor.execute(select_zones_table)

            rows = cursor.fetchall()
            for row in rows:
                list_row.append(row)
                #print(row)
                print(list_row)
                print("@"*20)

    finally:
        connection.close()
        print("connection closed")
        print("#"*20)

except Exception as ex:
    print("connections resused")
    print(ex)
