from app.api import medcive
from flask import Flask
from flask import render_template,make_response
from flask import Flask, request, redirect, url_for
import client
import config  #config file for Apimedic API
import requests
#-----connection with apimedic api------#

class PriaidDiagnosisClientDemo:
    def __init__(self):
        username = config.username
        password = config.password
        authUrl = config.priaid_authservice_url
        healthUrl = config.priaid_healthservice_url
        language = config.language
        self._printRawOutput = config.pritnRawOutput

        self._diagnosisClient = client.DiagnosisClient(username, password, authUrl, language, healthUrl)

#--------API 2---------#
#--------getting the diagnosis result according to symptom selected by user-------#

@medcive.route("/diagnosis", methods=['POST','GET'])
def diagnosis():
      pdcd=PriaidDiagnosisClientDemo()
      #if request.method == 'POST':
      selectedSymptom=request.form['symp']
      print(type(selectedSymptom))
      gender=request.form['gender']
      yob=request.form['yob']
      symptom=selectedSymptom.split(",")
      diagnosis = pdcd._diagnosisClient.loadDiagnosis(symptom,gender,yob)
      return render_template('diagnosis.html',dia=diagnosis)

