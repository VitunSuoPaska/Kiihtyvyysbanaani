import serial
import MySQLdb


def store_to_db(db1):
	#store to db
	print ("to db")

def main():
	db = MySQLdb.connect(host="sql11.freemysqlhosting.net", user="sql11155651", passwd="uwh45VlDHi",port =3306, db="sql11155651")
	cur = db.cursor()
	ser = serial.Serial('/dev/rfcomm0')

	buffer = ""
	while ser.is_open():
		buffer=ser.readline()
		if buffer!=""
			# add handling and farmatting the string properly
			store_to_db(db)
			buffer = ""

	db.close()
	ser.close()


if __name__ == "__main__": main()
#input()