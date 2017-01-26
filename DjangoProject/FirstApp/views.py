from django.shortcuts import render
from django.http import HttpResponse

import MySQLdb

db = MySQLdb.connect(host="sql11.freemysqlhosting.net", user="sql11155651", passwd="uwh45VlDHi",port =3306, db="sql11155651")

cur = db.cursor()

cur.execute("SELECT * FROM Acceleration")

test = ""
i=1

for row in cur.fetchall():
    test = test +"Data" +str(i) +" " + row[1] +"<br>"
    i = i+1

db.close()

test2 = "<html><head>Welcome to diz mothafucking webiste</head><br><br><body>bananas are currently insane af here have some data!<br>%s</body></html>" %test

def foo(request):
    return HttpResponse(test2)


# Create your views here.
