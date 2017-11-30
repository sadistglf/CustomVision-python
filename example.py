import httplib, urllib, base64
import CustomVisionPredictor

# fingerprint predictors
pred_key = "PREDICTION_KEY"
app_key = "APP_KEY"
iterationId = "ITERATION_ID"
appname = "APPNAME"

# Create the custom vision predictor
CVP = CustomVisionPredictor.CustomVisionPredictor(pred_key,app_key,iterationId,appname)

# predict using an image Url
data = CVP.predictUrl("https://vignette.wikia.nocookie.net/djangounchained/images/6/6e/Django2.jpg/revision/latest/scale-to-width-down/250?cb=20121231190413")
print(data)

# predict using a local file
image_path = 'LOCAL/PATH/TO/My.jpg'
with open(image_path, 'rb') as images_file:
	body = images_file
	data = CVP.predictImage(body)
	print(data)
