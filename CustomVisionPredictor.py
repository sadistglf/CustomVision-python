import httplib, urllib, base64

class CustomVisionPredictor:
	
	def __init__(self, pred_key, app_key, iterationId, appname):
		self.prediction_key = pred_key
		self.app_key = app_key
		self.iterationId = iterationId
		self.appname = appname

	
	def predictUrl(self,url):
		""" 
		This function configures and makes a prediction using an Url
		"""
		headers = {
		    'Content-Type':  'application/json',
		    'Prediction-key': self.prediction_key,
		}
		params = urllib.urlencode({
		    'iterationId': self.iterationId,
		    'application': self.appname,
		})
		body = {'Url': url}
		try:
			conn = httplib.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
			conn.request("POST", "/customvision/v1.0/Prediction/"+self.app_key+"/url?%s" % params, str(body), headers)
			response = conn.getresponse()
			data = response.read()
		except Exception as e:
			print("[Errno {}]".format(str(e)))
			data = "Error during predictImage: {}".format(str(e))
		return data
	
	def predictImage(self, image):
		""" 
		This funcion configures and makes a prediction using an opened image file 
		"""
		headers = {
		    'Content-Type':  'application/octet-stream',
		    'Prediction-key': self.prediction_key,
		}
		params = urllib.urlencode({
		    'iterationId': self.iterationId,
		    'application': self.appname,
		})
		body = image
		try:
			conn = httplib.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
			conn.request("POST", "/customvision/v1.0/Prediction/"+self.app_key+"/image?%s" % params, body, headers)
			response = conn.getresponse()
			data = response.read()
		except Exception as e:
			print("[Errno {}]".format(str(e)))
			data = "Error during predictImage: {}".format(str(e))
		return data


