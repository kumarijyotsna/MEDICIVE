from app.api import medcive
from flask import render_template
from flask import Flask, request
import infermedica_api
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import config_med #config file for infermedica API

#-------API 5-------#
#-------enter the symptoms xperienced by user----------#
@medcive.route("/search",methods=['POST','GET'])
def search():
      return render_template("search.html")


#--------getting the symptom result based on symptom entered by user in above step--------#
@medcive.route("/searched",methods=['POST','GET'])


def searched():
      config_med.setup_examples()#connecting to infermedica API to extract diagnosis for symtoms entered by user
      sym=request.form['search']
      #------extracting important keyword from sentence entered by user
      #example: Suppose use user entered "I have pain and fever"
      #So extracting words like pain and fever and searching for medical conditions user might be experiencing and then suggesting some more symptom   for user to select from and finally getting diagnosis result 
      words1 = word_tokenize(sym)
      tagged_sent = nltk.pos_tag(words1)
      pn=[]
      for word,pos in tagged_sent:
          print(word,pos)
          if pos=='NN' or pos == 'NNS' or pos== 'VBN' or pos== 'VBG':
             pn.append(word)
      #print(pn)
      api = infermedica_api.get_api()
      symptom=[]
      for word in pn:
         #print('Look for evidences containing phrase {}'.format(word))
         symptom_json=api.search(word)
         symptom.append(symptom_json)
      
      return render_template("select.html" , sym=symptom)

#--------getting the diagnosis result based on symptom selected by user in above step--------#
@medcive.route("/diagnosis_med", methods=['POST','GET'])
def diagnosis_med():
        selectedSymptom=request.form['symp'] #getting symptom selected by user in above step
        selectedSymptom=selectedSymptom.split(',')
        gender=request.form['gender']
        age=request.form['age']
        api = infermedica_api.API(app_id='APP_ID', app_key='APP_KEY') #insert app_key and app_id you get from infermedica api
        req = infermedica_api.Diagnosis(sex=gender, age=age)
        for sym in selectedSymptom:
           req.add_symptom(sym, 'present')
        
        req = api.diagnosis(req)
        return render_template("diagnosis_bot.html",req=req)
