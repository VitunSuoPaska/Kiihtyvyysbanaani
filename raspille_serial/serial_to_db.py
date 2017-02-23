import serial
import MySQLdb


def store_to_db(db, data):
    # store to db
    data = data.split(':')
    insert_query = """
    INSERT INTO Acceleration (GyroX,GyroY,GyroZ) VALUES(%s,%s,%s)
    """ % (float(data[0]), float(data[1]), float(data[2]))
    cur = db.cursor()
    cur.execute(insert_query)
    db.commit()
    print data[0]
    print insert_query


def main():
    db = MySQLdb.connect(host="sql11.freemysqlhosting.net",
                         user="sql11155651", passwd="uwh45VlDHi",
                         port=3306, db="sql11155651")
    # cur = db.cursor()
    # ser = serial.Serial('/dev/rfcomm0')
    ser = serial.Serial('/dev/ttyACM0')
    buffer1 = ""
    while ser.isOpen():
        buffer1 = ser.readline()
        if buffer1 != "":
            # add handling and farmatting the string properly
            store_to_db(db, buffer1)
            buffer1 = ""

    db.close()
    ser.close()


if __name__ == "__main__":
    main()
# input()
