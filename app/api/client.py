import requests
import hmac, hashlib
import base64
import json
from enum import Enum

#---client file for APIMEDIC API-------#

class DiagnosisClient:
    'Client class for priaid diagnosis health service'       
    def __init__(self, username, password, authServiceUrl, language, healthServiceUrl):
        self._handleRequiredArguments(username, password, authServiceUrl, healthServiceUrl, language)

        self._language = language
        self._healthServiceUrl = healthServiceUrl
        self._token = self._loadToken(username, password, authServiceUrl)


    def _loadToken(self, username, password, url):
        rawHashString = hmac.new(bytes(password), url.encode('utf-8')).digest()
        computedHashString = base64.b64encode(rawHashString).decode()

        bearer_credentials = username + ':' + computedHashString
        postHeaders = {
                'Authorization': 'Bearer {}'.format(bearer_credentials)
        }
        responsePost = requests.post(url, headers=postHeaders)

        data = json.loads(responsePost.text)
        return data
    def _handleRequiredArguments(self, username, password, authUrl, healthUrl, language):
        if not username:
            raise ValueError("Argument missing: username")

        if not password:
            raise ValueError("Argument missing: username")

        if not authUrl:
            raise ValueError("Argument missing: authServiceUrl")

        if not healthUrl:
            raise ValueError("Argument missing: healthServiceUrl")

        if not language:
            raise ValueError("Argument missing: language")
    def _loadFromWebService(self, action):
        extraArgs = "token=" + self._token["Token"] + "&format=json&language=" + self._language
        if "?" not in action:
            action += "?" + extraArgs
        else:
            action += "&" + extraArgs

        url = self._healthServiceUrl + "/" + action
        response = requests.get(url)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print ("----------------------------------")
            print ("HTTPError: " + e.response.text )
            print ("----------------------------------")
            raise

        try:
            dataJson = response.json()
        except ValueError:
            raise requests.exceptions.RequestException(response=response)

        data = json.loads(response.text)
        return data       
    def loadSymptoms(self):
        return self._loadFromWebService("symptoms")
    def loadDiagnosis(self, selectedSymptoms, gender, yearOfBirth):
        if not selectedSymptoms:
            raise ValueError("selectedSymptoms can not be empty")
        
        serializedSymptoms = json.dumps(selectedSymptoms)
        action = "diagnosis?symptoms={0}&gender={1}&year_of_birth={2}".format(serializedSymptoms, gender, yearOfBirth)
        return self._loadFromWebService(action)

