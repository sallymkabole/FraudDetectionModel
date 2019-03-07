import sys
import pandas 
from pandas import DataFrame
#from flask_login import UserMixin
from datetime import datetime
import MySQLdb
from flask import request, Flask, jsonify
from datetime import datetime
from app import db
import json
import MySQLdb as dbapi
import sys
import csv

app = Flask(__name__)



QUERY='SELECT id ,amount ,trans_at   FROM bank.transactions;'
db=dbapi.connect(host='localhost',user='root',passwd='@romeo123',db='bank')

cur=db.cursor()
cur.execute(QUERY)
result=cur.fetchall()

column_names = [i[0] for i in cur.description]
fp = open('output.csv','w')
myFile = csv.writer(fp, lineterminator = '\n') #use lineterminator for windows
myFile.writerow(column_names)
myFile.writerows(result)
fp.close()



	
  
