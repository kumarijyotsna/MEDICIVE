from app.api import medcive
from flask import Flask
from flask import render_template
from flask import Flask, request
import client
import config  #config file for Apimedic API

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


#----------API 1----------#
#------home page where we extract symptom from apidemic api--------#
@medcive.route("/",methods=['GET','POST'])
def symptom():
      pdcd=PriaidDiagnosisClientDemo()
      symptom = pdcd._diagnosisClient.loadSymptoms()
      return render_template('symptom.html',sym=symptom)












