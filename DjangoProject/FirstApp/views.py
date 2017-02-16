from django.shortcuts import render
from django.http import HttpResponse

import MySQLdb

def foo(request):
    
    #Try connecting to database and generating the webpage code.
    try:

        #Connect to database.
        db = MySQLdb.connect(host="sql11.freemysqlhosting.net", user="sql11155651", passwd="uwh45VlDHi",port =3306, db="sql11155651")

        #db = MySQLdb.connect(host="https://www.000webhost.com", user="id640745_oppilas", passwd="roger90",port =3306, db="id640745_acceleration")


        cur = db.cursor()

        cur.execute("SELECT * FROM Acceleration ORDER BY Time DESC LIMIT 10")

        rivi = []
        rivi2 = []
        rivi3 = []
        rivi4 = []



        #Read database data and save it.
        for row in cur.fetchall():
            rivi.append(str(row[0]))
            rivi2.append(str(row[1]))
            rivi3.append(str(row[2]))
            rivi4.append(str(row[3]))
            
            
            

        #close database connection, we don't need it anymore.
        db.close()

        Table2 = ""
        #Generate Html Table code from the databasedata.
        for x in range (0, len(rivi)):
            Table = "<tr><td>%(x)s</td><td>%(y)s</td><td>%(z)s</td><td>%(c)s</td></tr>" % { "x" : str(rivi[x]), "y" : str(rivi2[x]), "z" : str(rivi3[x]), "c" : str(rivi4[x])}
            Table2 = Table2 + Table

        #Finalize html Table code.
        Table2 = Table2 + "</tbody></table></div></div></div></div>"

        #Read First part of the html webpage code.    
        with open ("/home/pi/DjangoProject/FirstApp/html.txt","r") as myfile:
            htmlcode1=myfile.read().replace("/n","")

        #Read Last part of the html webpage code.
        with open ("/home/pi/DjangoProject/FirstApp/html2.txt","r") as myfile:
            htmlcode2=myfile.read().replace("/n","")

        #Combine webpage codes.
        webPage = htmlcode1 +Table2 +htmlcode2


    #Let's Return Error message if something fails.
    except:
        webPage = "Sorry we not work today"

    return HttpResponse(webPage)

    #Send webpage code to the website.


        


# Create your views here.
