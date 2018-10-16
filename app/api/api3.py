from app.api.models import User
from app.api import medcive
import requests
from flask import render_template,make_response
from flask import Flask, request
from bs4 import BeautifulSoup
from app import db
import csv
import pandas as pd

#---------API 3----------#
#----getting suggestion based on user's diagnosis using web scrapping------#
@medcive.route("/treatment", methods=['POST', 'GET'])
def treatment():
      
      res = requests.get("https://www.emedexpert.com/lists/conditions.shtml")  #scrapping given url to extract the table of diasease and symptom
      soup = BeautifulSoup(res.content,'lxml')
      table = soup.find_all('table')[0] 
      df = pd.read_html(str(table))
      #for i in df:
      #     print(i[0],i[1])
      df[0].to_csv("web_scrapped.csv", index=False, quoting=csv.QUOTE_NONE,escapechar=' ') #storing the extracted data in csv file
      #------storing data in sqlite3 database-------#
      with open('web_scrapped.csv','r') as person_table:
           dr = csv.DictReader(person_table, delimiter=',')
           to_db = [[i["1"],i["0"]] for i in dr]
      
      for i in to_db:
             record=User(**{
                     'disease': i[1],
                     'medicine': i[0]
             })
             db.session.add(record)
      db.session.commit()
      dis=request.args.get('text')
      #print(dis)
      treat=User.query.filter_by(disease=dis).first()
      #print(treat.medicine)
      return render_template("treatment.html",treat=(treat.medicine))
