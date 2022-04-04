import json
from flask import Flask, request, jsonify
import pymysql.cursors
import pymongo

#for SQL conections
connection = pymysql.connect(host='localhost',
                             user='<username>',
                             password='<password>',
                             database='<Database_Name>',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

#for mongo conections
client = pymongo.MongoClient("<mongoDBConnectionString>")
db = client.NanotubeDB

app = Flask(__name__)

@app.route("/getDataUsingSql",methods=["GET"])
def getDataUsingSql():
    result = ""
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM cardataset limit 10"
        cursor.execute(sql)
        result = cursor.fetchall()
        result = str(result)
    return result


@app.route("/getdataUsingMongoDb",methods=["GET"])
def getdataUsingMongoDb():
    coll  = db.carbon
    data = {"result": str(list(coll.find().limit(100)))}
    return data


if __name__ == "__main__":
    app.run()
