import unittest
import sys
sys.path.append('/home/simmi/MEDICIVE') #specify the path of your project
import app
from flask import Flask
import api2
import api1
import api3
import api4
import api5
#------testing all APIs--------#
class TestApi(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		print("setUpClass")
	@classmethod
	def tearDownClass(cls):
		print("tearDownClass")
	def setUp(self):
		print('setUp')
		self.app = app.app.test_client()
	def tearDown(self):
		print('tearDown')
	def create_app(self):
		app = Flask(__name__)
		app.config['TESTING'] = True
     
		app.config['LIVESERVER_PORT'] = 8080
      
		app.config['LIVESERVER_TIMEOUT'] = 10
		return app
#-----testing API 1----------#
	def test_api1(self):
		print("Testing API 1.....")
		response=self.app.post('/')
		self.assertEqual(response.status_code, 200)

#-----testing API 2----------#
	def test_api2(self):
		print("Testing API 2......")
		pdcd=api2.PriaidDiagnosisClientDemo()
		data={'sym':unicode('238'), 'gender':'female', 'yob':'1997'}
		dia=pdcd._diagnosisClient.loadDiagnosis([238],'female','1997')

#-----testing API 3----------#
	def test_api5(self):
		print("Testing API 5.....")
		response=self.app.get("/search")
		self.assertEqual(response.status_code, 200)

#-----testing API 4----------#
	def test_api4(self):
		print("Testing API 4.....")
		response=self.app.get('/location')
		self.assertEqual(response.status_code, 200)


		

if __name__=="__main__":
	unittest.main()
